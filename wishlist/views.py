from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile


@login_required
def wishlist(request):
    """ A view to return the wishlist page """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = Wishlist.objects.filter(user_profile=user_profile)
    wishlist_count = user_wishlist.count()  # Get the count of wishlist items

    return render(request, 'wishlist/wishlist.html', {
        'user_wishlist': user_wishlist,
        'wishlist_count': wishlist_count  # Pass the count to the template
    })


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # Use get_or_create to avoid multiple queries
    wishlist_item, created = Wishlist.objects.get_or_create(
        user_profile=user_profile, product=product
    )

    if created:
        messages.success(
            request, f'{wishlist_item.product.name} added to Wishlist successfully!')
    else:
        messages.warning(
            request, f'{product.name} is already in your Wishlist.')

    return redirect(reverse('products'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove item from Wishlist when remove icon is clicked
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist_item = Wishlist.objects.get(user_profile=user_profile,
                                         product=product)
    wishlist_item.delete()
    messages.success(request, f'{product.name} has been successfully removed.')
    return redirect(reverse('products'))
