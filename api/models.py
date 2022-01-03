from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=63, verbose_name='Никнейм пользователя')
    avatar = models.ImageField(verbose_name='Аватар пользователя')
    about = models.TextField(verbose_name='"О себе" пользователя')


class AgeRating(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название возрастного рейтинга')
    description = models.TextField(verbose_name='Описание возрастного рейтинга')

    class Meta:
        verbose_name = 'Возрастной рейтинг'
        verbose_name_plural = 'Возрастные рейтинги'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название жанра')
    description = models.TextField(verbose_name='Описание жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Franchise(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название франшизы')

    class Meta:
        verbose_name = 'Франшиза'
        verbose_name_plural = 'Франшизы'

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя персонажа')
    description = models.TextField(verbose_name='Описание персонажа')

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'

    def __str__(self):
        return self.name


class Anime(models.Model):
    class Status(models.TextChoices):
        ANNOUNCED = 'AN', _('Анонсировано')
        ONGOING = 'ON', _('Онгоинг')
        RELEASED = 'RE', _('Вышедшее')

    name_rus = models.CharField(max_length=255, verbose_name='Русское название')
    name_jap = models.CharField(max_length=255, default='', verbose_name='Японское название')
    poster = models.ImageField(default='', verbose_name='Постер')
    genres = models.ManyToManyField(Genre, related_name='anime', verbose_name='Жанры')
    characters = models.ManyToManyField(Character, related_name='anime', verbose_name='Персонажи')
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, verbose_name='Франшиза')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.ANNOUNCED)
    age_rating = models.ForeignKey(AgeRating, on_delete=models.CASCADE, verbose_name='Возрастной статус')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание аниме')
    number_of_episodes = models.PositiveSmallIntegerField(verbose_name='Количество эпизодов', default=0)

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Аниме')
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка пользователя', blank=True, null=True)
    number_of_episodes_watched = models.PositiveSmallIntegerField(verbose_name='Количество просмотренных эпизодов',
                                                                  default=0)
    view_status = models.CharField(max_length=2, choices=ViewStatus.choices, default=ViewStatus.PLANNED)
