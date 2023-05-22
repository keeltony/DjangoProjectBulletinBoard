from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView

from .forms import SignUpForm, UserActivationForm, send_mail_user_code
from Board.models import Response


@login_required()
def UserProfile(request):
    """Представление прфиля пользователя"""
    user = request.user
    response_info = Response.objects.filter(ads__author=User.objects.get(pk=user.pk)).filter(status=False)
    activate = user.groups.filter(name='Ads_create_update').exists()

    return render(request, 'account/UserProfile.html', {'user': user, 'response_info': response_info,
                                                        'activate': activate})


class SignUp(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = SignUpForm
    success_url = '/accounts/profile/'
    template_name = 'registration/signup.html'


@login_required()
def user_activate_pofile(request):
    """Активация профиля пользователя"""
    form = UserActivationForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data.get('code')
        user = request.user
        if user.userverification.code == code:
            user.groups.add(Group.objects.get(name='Ads_create_update'))
            return HttpResponseRedirect('/accounts/profile/')

    return render(request, 'account/user_account_activate.html', {'form': form})


@login_required()
def resending_email(request):
    """Повторная отправка пароля пользователю"""
    user = request.user
    send_mail_user_code(user.username, user.userverification.code, user.email)
    return HttpResponseRedirect('/accounts/activation/')
