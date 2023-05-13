from django.shortcuts import render


def UserProfile(request):
    context = request.user
    return render(request, 'account/UserProfile.html', {'context': context})
