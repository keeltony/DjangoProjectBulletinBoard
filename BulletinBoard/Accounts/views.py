from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from .forms import SignUpForm
from Board.models import Response


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


@login_required()
def UserProfile(request):
    """Представление прфиля пользователя"""
    user = request.user
    response_info = Response.objects.filter(ads__author=User.objects.get(pk=user.pk)).filter(status=False)

    return render(request, 'account/UserProfile.html', {'user': user, 'response_info': response_info})


# def user_activete(request):
#     user = request.user
#     forms = UserActiveiteForm()
#     return render(request, 'account/account_inactive.html', {'user': user, 'forms': forms})
