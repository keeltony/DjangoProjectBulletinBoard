from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save


from .models import UserVerification


@receiver(post_save, sender=User)
def user_verification_email(user, **kwargs):
    """Отправка кода проверки пользователя на его email"""
    code = UserVerification.objects.get(user=User.objects.get(pk=user.pk)).code
    send_mail(
        subject='Код подверждения регистрации',
        message=f'Привет {user.username} код потверждения: {code}',
        from_email=None,
        recipient_list=[user.email]
    )
