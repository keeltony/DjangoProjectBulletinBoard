import requests
from django.forms import DateTimeInput
from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter

from .models import Response, Ads
from django_filters import CharFilter


class ResponseFilter(FilterSet):
    text = CharFilter(lookup_expr='icontains', label='Поиск по сообщению')

    # ads = ModelMultipleChoiceFilter(field_name='ads',
    #                                 queryset=,
    #                                 label='По обьявлению', conjoined=False
    #                                 )

    date_create = DateTimeFilter(field_name='date', lookup_expr='gt',
                                 label='По дате:',
                                 widget=DateTimeInput(
                                     format='%Y:%m:%d',
                                     attrs={'type': 'date'},)
                                 )
