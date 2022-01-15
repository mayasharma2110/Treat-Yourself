from django.contrib import admin
from .models import Product, Category, ProductReview, ProductRating


class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ('rating',
                       'totalrating',
                       'numberofratings',
                       )

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'totalrating',
        'numberofratings',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile',
        'product',
        'review',
        'date_created',
        'date_updated',
    )

    ordering = ('-date_updated',)


class ProductRatingAdmin(admin.ModelAdmin):

    list_display = (
        'user_profile',
        'product',
        'rating',
        'date_created',
        'date_updated',
    )

    ordering = ('-date_updated',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
