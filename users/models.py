from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    nickname = models.CharField(_('Никнейм пользователя'), max_length=63)
    avatar = models.ImageField(_('Аватар пользователя'))
    about = models.TextField(_('"О себе" пользователя'))
