from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model): 
    """
    A Wishlist model for users to keep track of their favourite products
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name='user_wishlist')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_profile', 'product')

    def __str__(self):
        return f"{self.user_profile.user.username}'s wishlist - {self.product.name}"
