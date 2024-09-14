from .models import Wishlist
from profiles.models import UserProfile

def wishlist_context(request):
    """Context processor to pass wishlist items and their count to all templates."""
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        wishlist_items = Wishlist.objects.filter(user_profile=user_profile)
        wishlist_count = wishlist_items.count()  # Get the count of wishlist items
    else:
        wishlist_items = []
        wishlist_count = 0

    return {
        'user_wishlist': wishlist_items,
        'wishlist_count': wishlist_count,  # Pass the count to the templates
    }
