from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

import random
from .models import UserVerification


def verification_code():
    return random.randint(10000, 99999)


def send_mail_user_code(user_name, code, email):
    send_mail(
        subject='Код потверждения регистрации',
        message=f'Доброго времени суток {user_name} \n'
                f'Ваш код потверждения: {code}',
        from_email=None,
        recipient_list=[email]
    )


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

    def save(self, commit=False):
        user = super().save(self)
        user.save()
        code = UserVerification.objects.create(user=user, code=verification_code())
        code.save()
        send_mail_user_code(user.username, code, user.email)
        return user


class UserActivationForm(forms.ModelForm):
    class Meta:
        model = UserVerification
        fields = ['code']
