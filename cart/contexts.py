from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# Function to retrieve and calculate the contents of the shopping cart


def cart_contents(request):
    # Initialize variables for storing cart details
    cart_items = []  # List to hold individual cart item details
    total = 0  # Total price of all items in the cart
    product_count = 0  # Total quantity of all products in the cart
    # Retrieve cart data from the session
    cart = request.session.get('cart', {})

    # Extract product IDs from the cart and fetch related Product objects from the database
    product_ids = [item_id for item_id in cart.keys()]
    products = Product.objects.filter(pk__in=product_ids)
    product_map = {product.pk: product for product in products}

    # Iterate through items in the cart to calculate totals and prepare cart item details
    for item_id, item_data in cart.items():
        # Get the product object using its ID
        product = product_map.get(int(item_id))
        if not product:
            continue  # Skip if the product does not exist

        # Check if the cart item is a simple integer (no color options)
        if isinstance(item_data, int):
            # Calculate total price and update product count
            total += item_data * product.price
            product_count += item_data
            # Add item details to cart_items list
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            # If there are color options, handle each color separately
            for colour, quantity in item_data['items_by_colour'].items():
                # Calculate total price and update product count for each color variant
                total += quantity * product.price
                product_count += quantity
                # Add item details including color to cart_items list
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'colour': colour,
                })

    # Determine if the order qualifies for free delivery
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Calculate delivery cost based on a standard percentage if below the threshold
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # Calculate how much more the user needs to spend to qualify for free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # Free delivery if the total exceeds the threshold
        delivery = 0
        free_delivery_delta = 0

    # Calculate the final total including delivery costs
    grand_total = delivery + total

    # Prepare context with all cart-related data
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    # Return the context to be used across templates
    return context
