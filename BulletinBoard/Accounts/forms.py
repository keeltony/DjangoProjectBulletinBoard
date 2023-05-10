from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group

class CustomCreateUser(SignupForm):

    def save(self, request):
        user = super().save(request)
        # group = Group.objects.get('Ads_create_update')
        # group.user_set.add(user)
        return user
