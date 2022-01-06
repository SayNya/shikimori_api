from rest_framework import serializers
from .models import Anime


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
