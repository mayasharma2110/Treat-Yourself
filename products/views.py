from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, ProductReview, ProductRating
from .forms import ProductForm, ProductReviewForm, ProductRatingForm
from profiles.models import UserProfile


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # if the user sorts the products
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

    # if user uses the search bar
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
            products = products.filter(queries)

    # if user clicks on a specific category from navbar
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # derive discounted price for the product
    disc_price = round(Decimal('.90')*Decimal(product.price), 2)

    # reviews for the product
    product_reviews = product.reviews.all()

    if product_reviews.exists():
        any_reviews = True
    else:
        any_reviews = False

    # if the user logged in has rated/reviewed this product
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        product_ratings = product.ratings.all()
        user_reviewed = product_reviews.filter(user_profile=profile).exists()
        user_rated = product_ratings.filter(user_profile=profile).exists()
    else:
        user_reviewed = False
        user_rated = False

    context = {
        'product': product,
        'disc_price': disc_price,
        'product_reviews': product_reviews,
        'any_reviews': any_reviews,
        'user_reviewed': user_reviewed,
        'user_rated': user_rated,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can add a product.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        # check if form is valid
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        # if form is not valid
        else:
            messages.error(request, 'Failed to add product. ' +
                           'Please ensure the form is valid.')
    # get form
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can edit a product.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        # check if form is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        # form is not valid
        else:
            messages.error(request, 'Failed to update product.' +
                           'Please ensure the form is valid.')
    # get the form
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can delete a product.')
        return redirect(reverse('home'))

    # get the product and delete it
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a review of a product """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        form = ProductReviewForm(request.POST)
        form_data = {
            'review': request.POST['review'],
        }
        productreview_form = ProductReviewForm(form_data)
        # check if form is valid
        if productreview_form.is_valid():
            productreview = productreview_form.save(commit=False)
            productreview.product = product
            productreview.user_profile = profile
            productreview.save()
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product.id]))
        # form is not valid
        else:
            messages.error(request, 'Failed to add product review. ' +
                           'Please ensure the form is valid.')
    else:
        # check if the user has already made a review
        # for this product previously
        # if so redirect back to product page with an error message
        profile = UserProfile.objects.get(user=request.user)
        product_reviews = product.reviews.all()
        if product_reviews.filter(user_profile=profile).exists():
            messages.error(request, "You have already reviewed " +
                           "this product. You can update your " +
                           "review from below or your profile!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            form = ProductReviewForm()

    template = 'products/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Edit a review of a product """

    review = get_object_or_404(ProductReview, pk=review_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST, instance=review)
        # check if form is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product review!')
            return redirect(reverse('product_detail',
                                    args=[review.product.id]))
        # form is not valid
        else:
            messages.error(request, 'Failed to update product review.' +
                           'Please ensure the form is valid.')
    # get form
    else:
        form = ProductReviewForm(instance=review)
        messages.info(request, 'You are editing your review for' +
                      f'{review.product.name}')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review of a product """

    # get the review and delete it
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    review.delete()
    messages.success(request, 'Product review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def add_rating(request, product_id):
    """ Add a rating of a product """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        form = ProductRatingForm(request.POST)
        form_data = {
            'rating': int(request.POST['rating']),
        }
        productrating_form = ProductRatingForm(form_data)
        # check if form is valid
        if productrating_form.is_valid():
            productrating = productrating_form.save(commit=False)
            productrating.product = product
            productrating.user_profile = profile
            productrating.save()
            # feed this rating into info product rating, totalrating
            # and numberofratings fields
            product.numberofratings += 1
            product.totalrating += int(productrating.rating)
            product.rating = round(product.totalrating/product.numberofratings, 2)  # noqa
            product.save()
            # return user back to this product detail page
            messages.success(request, 'Successfully added product rating!')
            return redirect(reverse('product_detail', args=[product.id]))
        # form is not valid
        else:
            messages.error(request, 'Failed to add product review. ' +
                           'Please ensure the form is valid.')
    else:
        # check if the user has already made a rating
        # for this product previously
        # if so redirect back to product page with an error message
        profile = UserProfile.objects.get(user=request.user)
        product_ratings = product.ratings.all()
        if product_ratings.filter(user_profile=profile).exists():
            messages.error(request, "You have already rated " +
                           "this product. You can update your " +
                           "rating from your profile!")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            form = ProductRatingForm()

    template = 'products/add_rating.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_rating(request, rating_id):
    """ Update a rating of a product """

    rating = get_object_or_404(ProductRating, pk=rating_id)
    old_user_rating = int(rating.rating)
    product = rating.product

    if request.method == 'POST':
        form = ProductRatingForm(request.POST, instance=rating)
        # check if form is valid
        if form.is_valid():
            # feed this rating into info product rating, totalrating
            # and numberofratings fields
            old_totalrating = product.totalrating
            new_user_rating = int(request.POST['rating'])
            product.totalrating = old_totalrating - old_user_rating + new_user_rating  # noqa
            product.rating = round(product.totalrating/product.numberofratings, 2)  # noqa
            product.save()
            form.save()
            messages.success(request, 'Successfully updated product rating!')
            return redirect(reverse('product_detail',
                                    args=[rating.product.id]))
        # form is not valid
        else:
            messages.error(request, 'Failed to update product review.' +
                           'Please ensure the form is valid.')
    # get the form
    else:
        form = ProductRatingForm(instance=rating)
        messages.info(request, 'You are editing your rating for' +
                      f'{rating.product.name}')

    template = 'products/edit_rating.html'
    context = {
        'form': form,
        'rating': rating,
    }

    return render(request, template, context)


@login_required
def delete_rating(request, rating_id):
    """ Update a rating of a product """

    # get the rating and delete it
    rating = get_object_or_404(ProductRating, pk=rating_id)
    old_user_rating = int(rating.rating)
    product = rating.product
    old_totalrating = product.totalrating

    # feed this rating into info product rating, totalrating
    # and numberofratings fields
    product.totalrating = old_totalrating - old_user_rating
    product.numberofratings -= 1
    if product.numberofratings > 0:
        product.rating = round(product.totalrating/product.numberofratings, 2)
    else:
        product.rating = 0
    product.save()
    rating.delete()
    messages.success(request, 'Product rating deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
