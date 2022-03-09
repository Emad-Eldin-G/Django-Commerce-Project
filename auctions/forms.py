from dataclasses import fields
from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ["User", 'Title', 'Image', 'Details', 'Price', 'Category']