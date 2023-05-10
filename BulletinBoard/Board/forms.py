from django import forms
from .models import Ads


class CreateAdsForms(forms.ModelForm):
    class Meta:
        model = Ads
        fields = [
            'title',
            'text',
            'category',
            'upload',
        ]
