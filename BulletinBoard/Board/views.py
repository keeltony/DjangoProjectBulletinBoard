from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ads
from .forms import CreateAdsForms
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage


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


class DetailAds(generic.DetailView):
    model = Ads
    template_name = 'board/DetailAds.html'
    context_object_name = 'DetailAds'


class EditingAds(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Ads
    template_name = 'board/EditingAds.html'
    context_object_name = 'EditingAds'
    permission_required = ('Board.add_ads', 'Board.change_ads')


@login_required
def response_button(request, pk):
    user = request.user
    ads = Ads.objects.get(pk=pk)
    ads_user = ads.author
    email = EmailMessage(subject=ads.title, message='message', to=ads_user.email)
    email.send()
    return render(request, template_name='board/ResponseButton.html')
