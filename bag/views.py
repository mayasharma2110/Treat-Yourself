from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if request.POST.get('type-quantity') == "subscribe-monthly":
        product_type = "subscribe-monthly"
        quantity = 1
        type_messages = "monthly subscription of"
    else:
        product_type = "one-off"
        quantity = int(request.POST.get('type-quantity'))
        type_messages = ""

    # item id is already in bag
    if item_id in list(bag.keys()):
        # if item id in bag with same type update the quantity
        if product_type in bag[item_id]['items_by_type'
                                        ].keys() and product_type == "one-off":
            quantity_add = int(request.POST.get('type-quantity'))
            quantity_old = bag[item_id]['items_by_type'][product_type]
            # dont allow users to add more than 10 of any item at a time,
            # if they try show an error message explaining the issue
            quantity = quantity_old + quantity_add
            if quantity > 10:
                messages.error(request, 'Sorry, you can only add a maximum ' +
                               'of 10 items of any one product!')
            else:
                bag[item_id]['items_by_type'][product_type] = quantity
                messages.success(request, 'Updated quantity of ' +
                                 f'{product.name} to {quantity} in your bag.')
        # users can only have 1 subscription per product in the bag
        elif product_type in bag[item_id]['items_by_type'].keys() and product_type == "subscribe-monthly":  # noqa
            messages.error(request, 'Sorry, you can only have 1 ' +
                           'subscription of any one product!')
        # if item id in bag with different type add this in also
        else:
            bag[item_id]['items_by_type'][product_type] = quantity
            messages.success(request, f'Added {type_messages} ' +
                             f'{product.name} to your bag.')
    # item id is not already in bag add this in
    else:
        bag[item_id] = {"items_by_type": {product_type: quantity}}
        messages.success(request, f'Added {type_messages} ' +
                         f'{product.name} to your bag.')

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)


def add_now(request, item_id):
    """ Add the product to bag of quantity 1 """

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    product_type = "one-off"
    quantity = 1
    type_messages = ""

    # item id is already in bag
    if item_id in list(bag.keys()):
        # if item id in bag with same type update the quantity
        if product_type in bag[item_id]['items_by_type'
                                        ].keys() and product_type == "one-off":
            quantity_add = 1
            quantity_old = bag[item_id]['items_by_type'][product_type]
            # dont allow users to add more than 10 of any item at a time,
            # if they try show an error message explaining the issue
            quantity = quantity_old + quantity_add
            if quantity > 10:
                messages.error(request, 'Sorry, you can only add a maximum ' +
                               'of 10 items of any one product!')
            else:
                bag[item_id]['items_by_type'
                             ][product_type] = quantity
                messages.success(request, 'Updated quantity of ' +
                                 f'{product.name} to {quantity} in your bag.')
        # if item id in bag with different type add this in also
        else:
            bag[item_id]['items_by_type'][product_type] = quantity
            messages.success(request, f'Added {type_messages} ' +
                             f'{product.name} to your bag.')
    # item id is not already in bag add this in
    else:
        bag[item_id] = {"items_by_type": {product_type: quantity}}
        messages.success(request, f'Added {type_messages} {product.name} ' +
                         'to your bag.')

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(reverse('products'))


def add_again(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    # print(f'req post is {request.POST}')

    product_type = request.POST['product_type']
    quantity = int(request.POST['quantity'])

    if product_type == "subscribe-monthly":
        type_messages = "monthly subscription of"
    else:
        type_messages = ""

    # print(item_id)
    # print(product_type)
    # print(quantity)

    # item id is already in bag
    if item_id in list(bag.keys()):
        # if item id in bag with same type update the quantity
        if type in bag[item_id]['items_by_type'
                                ].keys() and product_type == "one-off":
            quantity_add = quantity
            quantity_old = bag[item_id]['items_by_type'][product_type]
            # dont allow users to add more than 10 of any item at a time,
            # if they try show an error message explaining the issue
            quantity = quantity_old + quantity_add
            if quantity > 10:
                messages.error(request, 'Sorry, you can only add a maximum ' +
                               'of 10 items of any one product!')
            else:
                bag[item_id]['items_by_type'][product_type] = quantity
                messages.success(request, 'Updated quantity of ' +
                                 f'{product.name} to {quantity} in your bag.')
        # users can only have 1 subscription per product in the bag
        elif type in bag[item_id
                         ]['items_by_type'
                           ].keys(
                                  ) and product_type == "subscribe-monthly":
            messages.error(request, 'Sorry, you can only have 1 ' +
                           'subscription of any one product!')
        # if item id in bag with different type add this in also
        else:
            bag[item_id]['items_by_type'][product_type] = quantity
            messages.success(request, f'Added {type_messages} ' +
                             f'{product.name} to your bag.')
    # item id is not already in bag add this in
    else:
        bag[item_id] = {"items_by_type": {product_type: quantity}}
        messages.success(request, f'Added {type_messages} ' +
                         f'{product.name} to your bag.')

    request.session['bag'] = bag
    # print(request.session['bag'])
    return HttpResponse(status=200)


def adjust_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    product_type = "one-off"
    quantity = int(request.POST.get('type-quantity'))

    # update quantity of item
    bag[item_id]["items_by_type"][product_type] = quantity
    messages.success(request, f'Updated quantity of {product.name} ' +
                     f'to {quantity} in your bag.')

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    product_type = request.POST['product_type']

    if product_type == "subscribe-monthly":
        type_messages = "monthly subscription of"
    else:
        type_messages = ""

    try:
        bag = request.session.get('bag', {})
        # remove this item from bag
        del bag[item_id]['items_by_type'][product_type]
        # if no types with this item anymore then remove it from the bag
        if not bag[item_id]['items_by_type']:
            bag.pop(item_id)

        request.session['bag'] = bag
        messages.warning(request, f'Removed {type_messages} ' +
                         f'{product.name} from your bag.')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}.')
        return HttpResponse(status=500)
