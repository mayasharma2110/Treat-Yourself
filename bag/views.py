from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if request.POST.get('type-quantity') == "subscribe-monthly":
        type = "subscribe-monthly"
        quantity = 1
    else: 
        type = "one-off"
        quantity = int(request.POST.get('type-quantity'))

    # item id is already in bag
    if item_id in list(bag.keys()):
        # if item id in bag with same type update the quantity
        if type in bag[item_id]['items_by_type'].keys() and type == "one-off":
            quantity_add = int(request.POST.get('type-quantity'))
            quantity_old = bag[item_id]['items_by_type'][type]
            # dont allow users to add more than 10 of any item at a time, if they try show an error message explaining the issue
            quantity = quantity_old + quantity_add
            if quantity > 10:
                pass
            else:
                bag[item_id]['items_by_type'][type] = quantity
        # users can only have 1 subscription per product in the bag
        elif type in bag[item_id]['items_by_type'].keys() and type == "subscribe-monthly":
            pass
        # if item id in bag with different type add this in also
        else:
            bag[item_id]['items_by_type'][type] = quantity
    # item id is not already in bag add this in
    else:
        bag[item_id] = {"items_by_type": {type: quantity}}

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    bag = request.session.get('bag', {})
    type = "one-off"
    quantity = int(request.POST.get('type-quantity'))

    # update quantity of item
    bag[item_id]["items_by_type"][type] = quantity

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    type = request.POST['type']

    try:
        bag = request.session.get('bag', {})
        # remove this item from bag
        del bag[item_id]['items_by_type'][type]
        # if no types with this item anymore then remove it from the bag
        if not bag[item_id]['items_by_type']:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)