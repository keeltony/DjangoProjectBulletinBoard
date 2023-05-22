from django.urls import path
from .views import UserProfile, SignUp, user_activate_pofile, resending_email

urlpatterns = [
    path('profile/', UserProfile, name='UserProfile'),
    path('signup/', SignUp.as_view(), name='SignUp'),
    path('activation/', user_activate_pofile, name='UserActivation'),
    path('resending/email/', resending_email ,name='Resending_email')
]
