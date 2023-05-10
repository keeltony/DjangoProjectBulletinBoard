from django.urls import path
from .views import CreateAds

urlpatterns = [
    path('create/', CreateAds.as_view(), name='CreateAds')
]
