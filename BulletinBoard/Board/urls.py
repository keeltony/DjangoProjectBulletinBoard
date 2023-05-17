from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListAds.as_view(), name='ListAds'),
    path('create/', views.CreateAds.as_view(), name='CreateAds'),
    path('<int:pk>', views.DetailAds.as_view(), name='DetailAds'),
    path('editing/<int:pk>', views.EditingAds.as_view(), name='EditingAds'),
    path('response/', views.ResponseList.as_view(), name='response'),
    path('response/create/<int:pk>', views.ResponseButton.as_view(), name='ResponseButton'),
    path('response/delete/<int:pk>', views.ResponseDelete.as_view(), name='ResponseDelete'),
    path('response/success/<int:pk>', views.response_success, name='response_success'),

]
