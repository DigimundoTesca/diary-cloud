from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
