from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """ Create bag_items variable from the bag in session """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, info in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        for type, quantity in info['items_by_type'].items():
            price = Decimal(product.price)
            disc_price = round(Decimal('.90')*Decimal(product.price),2)
            if type == "subscribe-monthly":
                subtotal =  quantity*disc_price
                total += quantity*disc_price
            else:
                subtotal = quantity*price
                total += quantity*price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'type': type,
                'price': price,
                'disc_price': disc_price,
                'subtotal': subtotal,
            })
    # print(bag_items[0]['price'])
    # print(bag_items[0]['disc_price'])

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY)
        delivery = round(delivery, 2)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
