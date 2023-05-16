from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from celery import shared_task


@shared_task
def response_button_send_mail(title, text, ads_user, ads_email,
                              res_user, get_response_url):
    """Отправка сообщения автору при отклике на его обьявление"""

    subject = f'Привет {ads_user}, на твое обьявление \"{title}\" отправили отклик'

    text_content = (f'Пользователь {res_user} откликнулся на ваше обьявление \n'
                    f'<a href="http://127.0.0.1:8000/{get_response_url}">{title}</a>'
                    f'Соообщение: {text}'
                    )

    html_content = (f'Пользователь {res_user} откликнулся на ваше обьявление \n'
                    f'<a href="http://127.0.0.1:8000/{get_response_url}">{title}</a>'
                    f'Соообщение: {text}'
                    )

    from_email = settings.DEFAULT_FROM_EMAIL
    to = [ads_email]

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
