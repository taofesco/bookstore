from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart, BookOrder


@receiver(post_save, sender=Cart)
def adjust_stock(sender, instance, **kwargs):
    if not instance.active:
        # Decrement stock counts
        orders = BookOrder.objects.filter(cart=instance)
        for order in orders:
            book = order.book
            book.stock -= order.quantity
            book.save()
