from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):
    wishlist_items = []
    product_count = 0
    wishlist = request.session.get('wishlist', {})

    product_ids = [item_id for item_id in wishlist.keys()]
    products = Product.objects.filter(pk__in=product_ids)
    product_map = {product.pk: product for product in products}

    for item_id, item_data in wishlist.items():
        product = product_map.get(int(item_id))
        if not product:
            continue
        if isinstance(item_data, int):
            total += item_data * product.price
            product_count += item_data
            wishlist_items.append({
                'item_id': item_id,
                'product': product,
            })
        else:
            for colour, quantity in item_data['items_by_colour'].items():
                product_count += quantity
                wishlist_items.append({
                    'item_id': item_id,
                    'product': product,
                    'colour': colour,
                })

    context = {
        'wishlist_items': wishlist_items,
        'product_count': product_count,
    }

    return context
