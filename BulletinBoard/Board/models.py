from django.db import models
from django.contrib.auth.models import User


class Ads(models.Model):
    TYPE = (
        ('TK', 'Tank'),
        ('HL', 'Healer'),
        ('DD', 'Damage dealer'),
        ('TR', 'Trader'),
        ('GM', 'Guild master'),
        ('QG', 'Quest giver'),
        ('WS', 'Warsmith'),
        ('TN', 'Tanner'),
        ('PM', 'Potion maker'),
        ('SM', 'Spell master'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    category = models.CharField(max_length=2, choices=TYPE, default='TK')
    upload = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return (f'{self.title}')


class Response(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)
