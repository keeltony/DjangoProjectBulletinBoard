from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import ConfirmEmailView
from allauth.account.decorators import verified_email_required


@login_required()
def UserProfile(request):
    context = request.user
    return render(request, 'account/UserProfile.html', {'context': context})



