from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ads
from .forms import CreateAdsForms


# Create your views here.

class CreateAds(LoginRequiredMixin, generic.CreateView):
    model = Ads
    form_class = CreateAdsForms
    template_name = 'board/CreateAds.html'
    context_object_name = 'CreateAds'


