from rest_framework import serializers
from .models import *


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'name_rus', 'name_jap', 'slug']
