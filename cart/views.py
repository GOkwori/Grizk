from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ 
    Add a quantity of the specified product to the shopping cart 
    """
    # Retrieve the product by its ID, or return a 404 if not found
    product = get_object_or_404(Product, pk=item_id)
    # Get the quantity of the product to add from the POST request
    quantity = int(request.POST.get('quantity'))
    # Retrieve the redirect URL from the form to return the user to the same page after adding
    redirect_url = request.POST.get('redirect_url')
    # Get the color of the product (if applicable) from the POST request
    colour = request.POST.get('product_colour', None)
    # Get the current cart from the session (or initialize it as an empty dictionary if none exists)
    cart = request.session.get('cart', {})

    # If a color is specified, handle the product with color variants
    if colour:
        # Initialize color variants if the item ID is not yet in the cart
        if item_id not in cart:
            cart[item_id] = {'items_by_colour': {}}
        # Update the quantity if the product and color combination already exists in the cart
        if colour in cart[item_id]['items_by_colour']:
            cart[item_id]['items_by_colour'][colour] += quantity
            messages.success(
                request, f'Updated colour {colour.upper()} {product.name} quantity to {cart[item_id]["items_by_colour"][colour]}')
        else:
            # Add the color variant if it does not exist in the cart
            cart[item_id]['items_by_colour'][colour] = quantity
            messages.success(
                request, f'Added colour {colour.upper()} {product.name} to your cart')
    else:
        # Handle products without color variants
        if item_id in cart:
            # Update the quantity if the product already exists in the cart
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            # Add the product if it is not yet in the cart
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    # Save the updated cart back into the session
    request.session['cart'] = cart
    # Redirect back to the provided URL
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ 
    Adjust the quantity of the specified product to the specified amount 
    """
    # Retrieve the product by its ID, or return a 404 if not found
    product = get_object_or_404(Product, pk=item_id)
    # Get the desired quantity from the POST request
    quantity = int(request.POST.get('quantity'))
    # Get the color of the product (if applicable) from the POST request
    colour = request.POST.get('product_colour', None)
    # Get the current cart from the session
    cart = request.session.get('cart', {})

    # If a color is specified, handle adjustments for color variants
    if colour:
        if item_id in cart and colour in cart[item_id]['items_by_colour']:
            if quantity > 0:
                # Update the quantity if the specified amount is greater than zero
                cart[item_id]['items_by_colour'][colour] = quantity
                messages.success(
                    request, f'Updated colour {colour.upper()} {product.name} quantity to {cart[item_id]["items_by_colour"][colour]}')
            else:
                # Remove the color variant if the specified amount is zero
                del cart[item_id]['items_by_colour'][colour]
                # Remove the entire item if no color variants are left
                if not cart[item_id]['items_by_colour']:
                    cart.pop(item_id)
                messages.success(
                    request, f'Removed colour {colour.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            # Update the quantity if the specified amount is greater than zero
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            # Remove the product if the specified amount is zero
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    # Save the updated cart back into the session
    request.session['cart'] = cart
    # Redirect to the cart view
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ 
    Remove the item from the shopping cart 
    """
    try:
        # Retrieve the product by its ID, or return a 404 if not found
        product = get_object_or_404(Product, pk=item_id)
        # Get the color of the product (if applicable) from the POST request
        colour = request.POST.get('product_colour', None)
        # Get the current cart from the session
        cart = request.session.get('cart', {})

        # If a color is specified, handle removal of the specific color variant
        if colour:
            if item_id in cart and colour in cart[item_id]['items_by_colour']:
                # Remove the color variant
                del cart[item_id]['items_by_colour'][colour]
                # Remove the entire item if no color variants are left
                if not cart[item_id]['items_by_colour']:
                    cart.pop(item_id)
                messages.success(
                    request, f'Removed colour {colour.upper()} {product.name} from your cart')
        else:
            # Remove the product if no color is specified (i.e., it has no color variants)
            if item_id in cart:
                cart.pop(item_id)
                messages.success(
                    request, f'Removed {product.name} from your cart')

        # Save the updated cart back into the session
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        # Catch any unexpected errors and provide an error message
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
