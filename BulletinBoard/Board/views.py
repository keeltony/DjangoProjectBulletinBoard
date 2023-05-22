from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect

from django.core.exceptions import PermissionDenied

from .models import Ads, Response
from .forms import CreateAdsForms, ResponseButtonForms
from .filters import ResponseFilter


class ListAds(generic.ListView):
    """ Показ всех обьявлений пользователей """

    model = Ads
    template_name = 'board/ListAds.html'
    ordering = '-date_create'
    context_object_name = 'ListAds'
    paginate_by = 5


class CreateAds(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    """Создание обьявления зарегистрированым пользователем"""

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
    """Полная информация по обьявлению"""

    model = Ads
    template_name = 'board/DetailAds.html'
    context_object_name = 'DetailAds'


class EditingAds(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    """"Редактирование обьявление для пользователя чье обьявлнеие
    обьявления других пользователей не редактируются """

    model = Ads
    template_name = 'board/EditingAds.html'
    context_object_name = 'EditingAds'
    permission_required = ('Board.add_ads', 'Board.change_ads')
    form_class = CreateAdsForms

    def form_valid(self, form):
        if form.instance.author != self.request.user:
            raise PermissionDenied
        else:
            return super().form_valid(form)


class ResponseButton(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    """ Отправка отклика на обьявление другого пользователя """

    model = Response
    form_class = ResponseButtonForms
    template_name = 'board/ResponseButton.html'
    context_object_name = 'ResponseButton'
    success_url = reverse_lazy('ListAds')
    permission_required = ('Board.add_ads', 'Board.change_ads')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ads = Ads.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class ResponseDelete(LoginRequiredMixin, generic.DeleteView):
    """Удаление откликов пользователей которые откликнулись на обьявлнеие
    пользователя"""

    model = Response
    template_name = 'board/ResponseDelete.html'
    context_object_name = 'ResponseDelete'
    success_url = '/board/response/'




@login_required()
def response_success(request, pk):
    """Представление на принятия отклика, так же
    отправляет сообщение на email"""

    user = request.user
    response = Response.objects.get(pk=pk)
    if user == response.ads.author:
        response.status = True
        response.save()
        send_mail(
            subject=f'Пользователь {user} принял ваше предложение',
            message=f'Ваш отклик на обьявление {response.ads} было принято',
            from_email=None,
            recipient_list=[response.author.email]
        )
        return HttpResponseRedirect(reverse_lazy('UserProfile'))


class ResponseList(generic.ListView):
    """приватная страница с откликами на обьявления пользователя"""

    model = Response
    template_name = 'board/Response.html'
    context_object_name = 'Response'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponseFilter(self.request.GET, queryset=Response.objects.filter(
            ads__author=self.request.user).order_by('-date_create'))
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['response'] = Response.objects.filter(ads__author=self.request.user).filter(status=False)
        return context
