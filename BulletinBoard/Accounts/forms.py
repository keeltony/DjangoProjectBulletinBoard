from allauth.account.forms import SignupForm
from django import forms


class CastomCreateUser(SignupForm):

    def save(self, request):
        user = super().save(request)
        return user
