from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview, ProductRating


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'sku', 'name', 'description', 'price', 'image_url', 'image')
   
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ('review',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductRatingForm(forms.ModelForm):

    class Meta:
        model = ProductRating
        fields = ('rating',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
