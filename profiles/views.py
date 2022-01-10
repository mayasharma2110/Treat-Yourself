from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile1 = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile1)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Failed to update profile. ' +
                           'Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile1)

    #orders made by the user
    orders = profile1.orders.all()

    # reviews made by user
    user_reviews = profile1.reviews.all()

    if user_reviews.exists():
        any_reviews = True
    else:
        any_reviews = False

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile1,
        'user_reviews': user_reviews,
        'any_reviews': any_reviews,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
