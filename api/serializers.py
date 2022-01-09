from rest_framework import serializers
from .models import Anime, CartAnime


class AnimeForMainMenuSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj):
        return f'{obj.description[:60]}...'

    class Meta:
        model = Anime
        fields = [
            'id',
            'name_rus',
            'poster',
            'slug',
            'description'
        ]


class AnimeDetailsSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    type = serializers.CharField(source='get_type_display')
    genres = serializers.StringRelatedField(many=True)
    age_rating = serializers.StringRelatedField()

    class Meta:
        model = Anime
        fields = '__all__'


class AnimeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = (
            'id',
            'name_rus',
            'slug',
            'number_of_episodes'
        )


class CartAnimeForProfileSerializer(serializers.ModelSerializer):
    view_status = serializers.CharField(source='get_view_status_display')
    anime = AnimeProfileSerializer()

    class Meta:
        model = CartAnime
        fields = (
            'id',
            'anime',
            'rating',
            'number_of_episodes_watched',
            'view_status'
        )


class CartAnimeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartAnime
        fields = (
            'id',
            'rating',
            'number_of_episodes_watched',
            'view_status'
        )
