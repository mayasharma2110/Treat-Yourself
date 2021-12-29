from django.shortcuts import render, redirect

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
        bag[item_id] = {"type": type, "quantity": quantity}
    else:
        type = "one-off"
        quantity = int(request.POST.get('type-quantity'))
        if item_id in list(bag.keys()):
            quantity1 = bag[item_id]["quantity"] + quantity
            bag[item_id] = {"type": type, "quantity": quantity1}
        else:
            bag[item_id] = {"type": type, "quantity": quantity}

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)