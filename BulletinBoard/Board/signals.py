from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Response
from .tasks import response_button_send_mail


@receiver(post_save, sender=Response)
def responseButton(instance, **kwargs):
    """Отправка сообщения автору при отклике на его обьявление"""

    title = instance.ads.title
    ads_user = instance.ads.author.username
    ads_email = instance.ads.author.email
    res_user = instance.author.username


    response_button_send_mail.delay(title, instance.text,
                                    ads_user, ads_email, res_user,
                                    instance.ads.get_response_url())
