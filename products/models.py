from django.db import models
from profiles.models import UserProfile

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    totalrating = models.IntegerField(null=True, blank=True)
    numberofratings = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     related_name="reviews")
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name="reviews")
    review = models.CharField(max_length=254)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review
