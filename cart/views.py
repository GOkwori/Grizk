from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view to return the cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the cart """
    product = get_object_or_404(
        Product, pk=item_id)  # Ensure the product is retrieved

    # Default to 1 if quantity is not provided
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse(
        'view_cart'))  # Default redirect to cart view
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}.')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(
        Product, pk=item_id)  # Ensure the product is retrieved

    # Default to 1 if quantity is not provided
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}.')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart.')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        # Ensure the product is retrieved
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        messages.success(request, f'Removed {product.name} from your cart.')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
