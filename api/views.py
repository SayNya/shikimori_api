from rest_framework import generics
from .models import *
from .serializers import AnimeSerializer


class AnimeView(generics.ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
