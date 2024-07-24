from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    try:
        return price * quantity
    except (TypeError, ValueError):
        return 0
