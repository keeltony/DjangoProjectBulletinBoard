from django.urls import path
from .views import UserProfile

urlpatterns = [
    path('profile/', UserProfile, name='UserProfile'),
    # path('inactive/', user_activete, name='user_activete')

]
