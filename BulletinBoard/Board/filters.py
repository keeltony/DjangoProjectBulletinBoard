from django.forms import DateTimeInput
from django import forms

from django_filters import FilterSet, DateTimeFilter, BooleanFilter, ModelMultipleChoiceFilter, CharFilter
from .models import Ads


class ResponseFilter(FilterSet):
    text = CharFilter(lookup_expr='icontains', label='Поиск по сообщению')

    date_create = DateTimeFilter(field_name='date', lookup_expr='gt',
                                 label='По дате:',
                                 widget=DateTimeInput(
                                     format='%Y:%m:%d',
                                     attrs={'type': 'date'}, )
                                 )

    ads = ModelMultipleChoiceFilter(field_name='ads',
                                    queryset=Ads.objects.all(),
                                    label='По обьявлению', conjoined=False
                                    )

    status = BooleanFilter(field_name='status', label='Принятые', widget=forms.CheckboxInput)
