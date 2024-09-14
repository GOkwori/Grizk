# wishlist/contexts.py

from .models import Wishlist
from profiles.models import UserProfile

def wishlist_context(request):
    """Context processor to pass wishlist items to all templates."""
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        wishlist_items = Wishlist.objects.filter(user_profile=user_profile)
    else:
        wishlist_items = []

    return {
        'user_wishlist': wishlist_items,
    }
