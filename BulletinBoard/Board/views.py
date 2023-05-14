from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives

from .models import Ads, Response
from .forms import CreateAdsForms, ResponseButtonForms


class ListAds(generic.ListView):
    model = Ads
    template_name = 'board/ListAds.html'
    ordering = '-date_create'
    context_object_name = 'ListAds'


class CreateAds(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Ads
    form_class = CreateAdsForms
    template_name = 'board/CreateAds.html'
    context_object_name = 'CreateAds'
    success_url = '/board/'
    permission_required = ('Board.add_ads', 'Board.change_ads')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailAds(LoginRequiredMixin, generic.DetailView):
    model = Ads
    template_name = 'board/DetailAds.html'
    context_object_name = 'DetailAds'


class EditingAds(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Ads
    template_name = 'board/EditingAds.html'
    context_object_name = 'EditingAds'
    permission_required = ('Board.add_ads', 'Board.change_ads')


class ResponseButton(LoginRequiredMixin, generic.CreateView):
    model = Response
    form_class = ResponseButtonForms
    template_name = 'board/ResponseButton.html'
    context_object_name = 'ResponseButton'
    success_url = reverse_lazy('ListAds')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ads = Ads.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)
