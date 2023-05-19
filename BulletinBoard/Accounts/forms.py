from django.contrib.auth.models import Group
from django.forms import ModelForm, CharField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import random
from .models import UserVerification


def verification_code():
    return random.randint(10000, 99999)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def save(self, request):
        user = super().save(request)
        user.save()
        user.groups.add(Group.objects.get(name='Ads_create_update'))
        code = UserVerification.objects.create(user=user, code=verification_code())
        code.save()
        return user


class UserActiveiteForm(ModelForm):
    model = UserVerification

    class Meta:
        fields = ['code']
