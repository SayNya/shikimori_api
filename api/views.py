from rest_framework import generics
from .models import *
from .serializers import AnimeForMainMenuSerializer, AnimeDetailsSerializer


class AnimeForMainMenuView(generics.ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeForMainMenuSerializer


class AnimeDetailsView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailsSerializer
    lookup_field = 'slug'
