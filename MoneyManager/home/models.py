from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICES = [
    ('gender', 'Gender'),
    ('profession', 'Profession')
]


class Choice(models.Model):
    field = models.CharField(max_length=100, choices=CHOICES)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


class UserInfo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='userinfo')
    income = models.BigIntegerField()
    profession = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
