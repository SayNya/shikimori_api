from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class AgeRating(models.Model):
    name = models.CharField(_('Название возрастного рейтинга'), max_length=255)
    description = models.TextField(_('Описание возрастного рейтинга'))

    class Meta:
        verbose_name = _('Возрастной рейтинг')
        verbose_name_plural = _('Возрастные рейтинги')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(_('Название жанра'), max_length=255)
    description = models.TextField(_('Описание жанра'))

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')

    def __str__(self):
        return self.name


class Franchise(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Название франшизы'))

    class Meta:
        verbose_name = _('Франшиза')
        verbose_name_plural = _('Франшизы')

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(_('Имя персонажа'), max_length=255)
    description = models.TextField(_('Описание персонажа'))

    class Meta:
        verbose_name = _('Персонаж')
        verbose_name_plural = _('Персонажи')

    def __str__(self):
        return self.name


class Anime(models.Model):
    class Status(models.TextChoices):
        ANNOUNCED = 'AN', _('Анонсировано')
        ONGOING = 'ON', _('Онгоинг')
        RELEASED = 'RE', _('Вышедшее')

    class Type(models.TextChoices):
        TV = 'TV', _('TV Сериал')
        FILM = 'FM', _('Фильм')
        OVA = 'OV', _('OVA')
        ONA = 'ON', _('ONA')
        SPECIAL = 'SP', _('Спешл')

    name_rus = models.CharField(_('Русское название'), max_length=255)
    name_jap = models.CharField(_('Японское название'), max_length=255, default='')
    poster = models.ImageField(_('Постер'), default='')
    genres = models.ManyToManyField(Genre, verbose_name=_('Жанры'), related_name='anime')
    characters = models.ManyToManyField(Character, verbose_name=_('Персонажи'), related_name='anime')
    franchise = models.ForeignKey(Franchise, verbose_name=_('Франшиза'), on_delete=models.CASCADE)
    status = models.CharField(_('Статус выхода'), max_length=2, choices=Status.choices, default=Status.ANNOUNCED)
    type = models.CharField(_('Тип аниме'), max_length=2, choices=Type.choices, default=Type.TV)
    age_rating = models.ForeignKey(AgeRating, verbose_name=_('Возрастной статус'), on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField(_('Описание аниме'))
    number_of_episodes = models.PositiveSmallIntegerField(_('Количество эпизодов'), default=0)

    class Meta:
        verbose_name = _('Аниме')
        verbose_name_plural = _('Аниме')

    def __str__(self):
        return self.name_rus


class CartAnime(models.Model):
    class ViewStatus(models.TextChoices):
        PLANNED = 'PL', _('Запланировано')
        WATCH = 'WA', _('Смотрю')
        VIEWED = 'VI', _('Просмотрено')
        REVIEW = 'RE', _('Пересматриваю')
        ABANDONED = 'AB', _('Брошено')
        POSTPONED = 'PO', _('Отложено')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Пользователь'), related_name='cart_anime',
                             on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, verbose_name=_('Аниме'), related_name='cart_anime', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(_('Оценка пользователя'), blank=True, null=True)
    number_of_episodes_watched = models.PositiveSmallIntegerField(_('Количество просмотренных эпизодов'), default=0)
    view_status = models.CharField(_('Статус просмотра'), max_length=2, choices=ViewStatus.choices,
                                   default=ViewStatus.PLANNED)

    def __str__(self):
        return f'{self.user} - {self.anime}'

    class Meta:
        verbose_name = _('Аниме для списка')
        verbose_name_plural = _('Аниме для списка')
