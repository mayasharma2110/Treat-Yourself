from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, ProductReview
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

    disc_price = round(Decimal('.90')*Decimal(product.price), 2)

    # reviews for the product
    product_reviews = product.reviews.all()

    if product_reviews.exists():
        any_reviews = True
    else:
        any_reviews = False

    context = {
        'product': product,
        'disc_price': disc_price,
        'product_reviews': product_reviews,
        'any_reviews': any_reviews,
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
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. ' +
                           'Please ensure the form is valid.')
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
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
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
            # print(productreview.id)
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product review. ' +
                           'Please ensure the form is valid.')
    else:
        # check if the user has already made a review
        # for this product previously
        # if so redirect back to product page with an error message
        profile = UserProfile.objects.get(user=request.user)
        product_reviews = product.reviews.all()
        # print(product_reviews.filter(user_profile=profile).exists())
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
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product review!')
            return redirect(reverse('product_detail', args=[review.product.id]))
        else:
            messages.error(request, 'Failed to update product review. Please ensure the form is valid.')
    else:
        form = ProductReviewForm(instance=review)
        messages.info(request, f'You are editing your review for {review.product.name}')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review of a product """

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
            # print(productrating.id)
            # feed this rating into info product rating, totalrating and numberofratings fields
            # print(product.numberofratings)
            product.numberofratings += 1
            product.totalrating += int(productrating.rating)
            product.rating = round(product.totalrating/product.numberofratings, 2)
            product.save()
            # print(product.numberofratings)
            # reutn user back to this product detail page
            messages.success(request, 'Successfully added product rating!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product review. ' +
                           'Please ensure the form is valid.')
    else:
        # check if the user has already made a rating
        # for this product previously
        # if so redirect back to product page with an error message
        profile = UserProfile.objects.get(user=request.user)
        product_ratings = product.ratings.all()
        # print(product_ratings.filter(user_profile=profile).exists())
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
