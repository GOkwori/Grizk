from django import template
from django.utils.html import format_html

# Register this file as a template tag library
register = template.Library()

# Custom template filter to calculate the subtotal
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    try:
        # Attempt to calculate the subtotal by multiplying price and quantity
        return price * quantity
    except (TypeError, ValueError):
        # If there is an error (e.g., invalid data types), return 0 as a fallback
        return 0
