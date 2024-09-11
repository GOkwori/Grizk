import stripe
import json
import time
import logging
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

logger = logging.getLogger(__name__)

class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        try:
            cust_email = order.email
            subject = render_to_string(
                'checkout/confirmation_emails/confirmation_email_subject.txt',
                {'order': order}
            )
            body = render_to_string(
                'checkout/confirmation_emails/confirmation_email_body.txt',
                {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
            )
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])
            logger.info(f'Confirmation email sent successfully to {cust_email}')
        except Exception as e:
            logger.error(f'Error sending confirmation email: {e}')

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.get('cart', '{}')
        save_info = intent.metadata.get('save_info', False)
        username = intent.metadata.get('username', 'AnonymousUser')

        try:
            stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        except stripe.error.StripeError as e:
            logger.error(f'Stripe error while retrieving charge: {e}')
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500
            )

        billing_details = stripe_charge.billing_details
        shipping_details = getattr(intent, 'shipping', None)
        grand_total = round(stripe_charge.amount / 100, 2)

        if shipping_details:
            shipping_details.address = {k: v if v != "" else None for k, v in shipping_details.address.items()}
        
        profile = None
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.default_town_or_city = shipping_details.address.city
                    profile.default_street_address1 = shipping_details.address.line1
                    profile.default_street_address2 = shipping_details.address.line2
                    profile.default_county = shipping_details.address.state
                    profile.save()
            except UserProfile.DoesNotExist:
                logger.warning(f'UserProfile not found for {username}')

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        try:
            order = Order.objects.create(
                full_name=shipping_details.name,
                user_profile=profile,
                email=billing_details.email,
                phone_number=shipping_details.phone,
                country=shipping_details.address.country,
                postcode=shipping_details.address.postal_code,
                town_or_city=shipping_details.address.city,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                county=shipping_details.address.state,
                original_cart=cart,
                stripe_pid=pid,
            )
            order_line_items = []
            for item_id, item_data in json.loads(cart).items():
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_items.append(OrderLineItem(order=order, product=product, quantity=item_data))
                else:
                    for size, quantity in item_data['items_by_size'].items():
                        order_line_items.append(OrderLineItem(order=order, product=product, quantity=quantity, product_size=size))
            OrderLineItem.objects.bulk_create(order_line_items)
        except Exception as e:
            logger.error(f'Error creating order: {e}')
            if order:
                order.status = 'failed'
                order.save()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500
            )

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        logger.warning(f"Payment failed for PaymentIntent {event.data.object.id}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
