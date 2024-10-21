# Import the template module from Django
from django import template

# Create an instance of the Library class to register custom template tags and filters
register = template.Library()

# Define a custom filter named 'calc_subtotal'


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Custom template filter to calculate the subtotal of an item.
    It multiplies the price by the quantity and returns the result.

    Args:
        price (float): The price of a single item.
        quantity (int): The quantity of items.

    Returns:
        float: The subtotal (price * quantity).
    """
    return price * quantity
