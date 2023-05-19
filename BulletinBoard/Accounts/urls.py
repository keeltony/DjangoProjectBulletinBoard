from django.urls import path
from .views import UserProfile, SignUp

urlpatterns = [
    path('profile/', UserProfile, name='UserProfile'),
    path('signup/', SignUp.as_view(), name='SignUp'),
    # path('inactive/', user_activete, name='user_activete')

]
