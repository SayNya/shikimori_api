from rest_framework import serializers
from .models import *


class AnimeForMainMenuSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return f'{obj.description[:60]}...'

    class Meta:
        model = Anime
        fields = ['id', 'name_rus', 'poster', 'slug', 'description']


class AnimeDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anime
        fields = '__all__'
