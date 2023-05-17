
from django.forms import DateTimeInput
from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter


from .models import Response
from django_filters import CharFilter


class ResponseFilter(FilterSet):

    text = CharFilter(lookup_expr='icontains', label='Text')

    ads = ModelMultipleChoiceFilter(
        field_name='ads',
        queryset=Response.objects.all().values_list('text'),
        label='Ads',
        conjoined=False
    )

    date_create = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y:%m:%d',
            attrs={'type': 'date'},
        )
    )
