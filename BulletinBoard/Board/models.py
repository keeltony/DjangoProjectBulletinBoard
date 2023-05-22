from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Ads(models.Model):
    TYPE = [
        ('TN', 'Танк'),
        ('HI', 'Хилы'),
        ('DD', 'ДД'),
        ('TO', 'Торговцы'),
        ('GI', 'Гилдмастеры'),
        ('KW', 'Квестгиверы'),
        ('KU', 'Кузнецы'),
        ('KO', 'Кожевники'),
        ('ZE', 'Зельевары'),
        ('MA', 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    category = models.CharField(max_length=2, choices=TYPE, default='TN')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    upload = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return (f'{self.title}')

    def get_response_url(self):
        return reverse('DetailAds', args=[str(self.pk)])


class Response(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'
