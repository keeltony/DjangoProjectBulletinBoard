from django.contrib.auth.models import Group
from django.forms import ModelForm, CharField

import random
from .models import UserVerification
from allauth.account.forms import SignupForm


def verification_code():
    return random.randint(10000, 99999)


class CustomCreateUser(SignupForm):

    def save(self, request):
        user = super().save(request)
        user.is_active = False
        user.save()
        user.groups.add(Group.objects.get(name='Ads_create_update'))
        code = UserVerification.objects.create(user=user, code=verification_code())
        code.save()
        return user


class UserActiveiteForm(ModelForm):
    model = UserVerification

    class Meta:
        fields = ['code']
