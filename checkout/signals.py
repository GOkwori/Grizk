from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import order_line_item


@receiver(post_save, sender=order_line_item)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=order_line_item)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
