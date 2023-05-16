from allauth.account.forms import SignupForm

from django.contrib.auth.models import Group

import random
from .models import UserVerification


def verification_code():
    return random.randint(10000, 99999)


class CustomCreateUser(SignupForm):

    def save(self, request):
        user = super().save(request)
        user.save()
        user.groups.add(Group.objects.get(name='Ads_create_update'))
        code = UserVerification.objects.create(user=user, code=verification_code())
        code.save()
        return user
