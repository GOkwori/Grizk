from typing import Iterable
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_reference = models.CharField(
        max_length=20, blank=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    date = models.DateField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_reference(self):
        """
        Generate a random, unique order reference using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added, accounting for delivery costs
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * \
                settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_reference:
            self.order_reference = self._generate_order_reference()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_reference


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_reference}'
