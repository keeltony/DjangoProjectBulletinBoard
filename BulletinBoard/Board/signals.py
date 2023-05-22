from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Response
from .tasks import response_button_send_mail


@receiver(post_save, sender=Response)
def responseButton(instance, **kwargs):
    """Отправка сообщения автору при отклике на его обьявление через celery"""

    title = instance.ads.title
    ads_user = instance.ads.author.username
    ads_email = instance.ads.author.email
    res_user = instance.author.username

    response_button_send_mail.delay(title, instance.text,
                                    ads_user, ads_email, res_user,
                                    instance.ads.get_response_url())


@receiver(post_delete, sender=Response)
def response_delete(instance, **kwargs):
    """Отправка сообщения при удалении автором обьявления отклика"""

    ads_user = instance.ads.author.username
    ads_title = instance.ads.title
    res_email = instance.author.email
    res_user = instance.author.username
    send_mail(
        subject=f'{res_user}, ваш отклик был удален',
        message=f'Позьзователь {ads_user} удалил ваш отклик со своего обьявления: "{ads_title}"',
        from_email=None,
        recipient_list=[res_email]
    )
