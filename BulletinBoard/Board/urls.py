from django.urls import path
from .views import CreateAds, ListAds, DetailAds, EditingAds, response_button

urlpatterns = [
    path('', ListAds.as_view(), name='ListAds'),
    path('create/', CreateAds.as_view(), name='CreateAds'),
    path('<int:pk>', DetailAds.as_view(), name='DetailAds'),
    path('editing/<int:pk>', EditingAds.as_view(), name='EditingAds'),
    path('response/<int:pk>', response_button, name='ResponseButton'),

]
