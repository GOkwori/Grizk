from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_wishlist(request):
    """ A view that renders the wishlist contents page """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add a quantity of the specified product to the shopping wishlist """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    colour = request.POST.get('product_colour', None)
    wishlist = request.session.get('wishlist', {})

    if colour:
        if item_id not in wishlist:
            wishlist[item_id] = {'items_by_colour': {}}
        if colour in wishlist[item_id]['items_by_colour']:
            wishlist[item_id]['items_by_colour'][colour] += quantity
            messages.success(
                request, f'Updated colour {colour.upper()} {product.name} quantity to {wishlist[item_id]["items_by_colour"][colour]}')
        else:
            wishlist[item_id]['items_by_colour'][colour] = quantity
            messages.success(
                request, f'Added colour {colour.upper()} {product.name} to your wishlist')
    else:
        if item_id in wishlist:
            wishlist[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {wishlist[item_id]}')
        else:
            wishlist[item_id] = quantity
            messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):
    """Remove the item from the shopping wishlist"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        colour = request.POST.get('product_colour', None)
        wishlist = request.session.get('wishlist', {})

        if colour:
            if item_id in wishlist and colour in wishlist[item_id]['items_by_colour']:
                del wishlist[item_id]['items_by_colour'][colour]
                if not wishlist[item_id]['items_by_colour']:
                    wishlist.pop(item_id)
                messages.success(
                    request, f'Removed colour {colour.upper()} {product.name} from your wishlist')
        else:
            if item_id in wishlist:
                wishlist.pop(item_id)
                messages.success(
                    request, f'Removed {product.name} from your wishlist')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
