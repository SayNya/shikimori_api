# Generated by Django 4.0 on 2022-01-03 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cartanime_profile_anime_number_of_episodes_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StarRating',
        ),
    ]