from django import forms
from .models import Ads, Response


class CreateAdsForms(forms.ModelForm):
    class Meta:
        model = Ads
        fields = [
            'title',
            'text',
            'category',
            'upload',
        ]


class ResponseButtonForms(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text'
        ]
