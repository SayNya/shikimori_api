from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    nickname = models.CharField(_('Никнейм пользователя'), max_length=63, default='', blank=True)
    avatar = models.ImageField(_('Аватар пользователя'), blank=True, null=True)
    about = models.TextField(_('"О себе" пользователя'), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = self.username
        super().save(*args, **kwargs)
