from django import forms
from form_app.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #exclude = ['created_at']  # Exclude the created_at field from the form
        
