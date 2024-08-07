from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = request.POST.get('product_colour', None)
    cart = request.session.get('cart', {})

    if colour:
        if item_id not in cart:
            cart[item_id] = {'items_by_colour': {}}
        if colour in cart[item_id]['items_by_colour']:
            cart[item_id]['items_by_colour'][colour] += quantity
            messages.success(
                request, f'Updated colour {colour.upper()} {product.name} quantity to {cart[item_id]["items_by_colour"][colour]}')
        else:
            cart[item_id]['items_by_colour'][colour] = quantity
            messages.success(
                request, f'Added colour {colour.upper()} {product.name} to your cart')
    else:
        if item_id in cart:
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    colour = request.POST.get('product_colour', None)
    cart = request.session.get('cart', {})

    if colour:
        if item_id in cart and colour in cart[item_id]['items_by_colour']:
            if quantity > 0:
                cart[item_id]['items_by_colour'][colour] = quantity
                messages.success(
                    request, f'Updated colour {colour.upper()} {product.name} quantity to {cart[item_id]["items_by_colour"][colour]}')
            else:
                del cart[item_id]['items_by_colour'][colour]
                if not cart[item_id]['items_by_colour']:
                    cart.pop(item_id)
                messages.success(
                    request, f'Removed colour {colour.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        colour = request.POST.get('product_colour', None)
        cart = request.session.get('cart', {})

        if colour:
            if item_id in cart and colour in cart[item_id]['items_by_colour']:
                del cart[item_id]['items_by_colour'][colour]
                if not cart[item_id]['items_by_colour']:
                    cart.pop(item_id)
                messages.success(
                    request, f'Removed colour {colour.upper()} {product.name} from your cart')
        else:
            if item_id in cart:
                cart.pop(item_id)
                messages.success(
                    request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
