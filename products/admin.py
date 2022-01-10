from django.contrib import admin
from .models import Product, Category, ProductReview


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

    # readonly_fields = ('user_profile',
    #                    'product',
    #                    'date',
    #                    'review'
    #                    )

    list_display = (
        'user_profile',
        'product',
        'review',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
