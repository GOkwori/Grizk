from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PLcnmFYVBBpwdrwg2sSST93D1jedel82gAtDMhARMQcGvDeG47BAX6Hgfc1SMVkrKoWownxscFaSf89r4s6A6sl00DYTyzPGL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
