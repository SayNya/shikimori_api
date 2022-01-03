from django.contrib.auth import get_user_model
from django.db import models

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


class Status(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название статуса')

    class Meta:
        verbose_name = 'Статус выхода'
        verbose_name_plural = 'Статусы выхода'

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
    name_rus = models.CharField(max_length=255, verbose_name='Русское название')
    name_jap = models.CharField(max_length=255, default='', verbose_name='Японское название')
    genres = models.ManyToManyField(Genre, related_name='anime', verbose_name='Жанры')
    characters = models.ManyToManyField(Character, related_name='anime', verbose_name='Персонажи')
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, verbose_name='Франшиза')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    age_rating = models.ForeignKey(AgeRating, on_delete=models.CASCADE, verbose_name='Возрастной статус')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание аниме')

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'

    def __str__(self):
        return self.name_rus


class StarRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Аниме')
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка')

    class Meta:
        verbose_name = 'Оценочный рейтинг'
        verbose_name_plural = 'Оценочные рейтинги'

    def __str__(self):
        return f'{self.user.username} - {self.anime.name_rus[:10]} - {self.rating}'
