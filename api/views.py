from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from .models import *
from .permissions import IsCartAnimeOwnerOrReadOnly
from .serializers import AnimeForMainMenuSerializer, AnimeDetailsSerializer, CartAnimeUserSerializer


class AnimeForMainMenuView(generics.ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeForMainMenuSerializer


class AnimeDetailsView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailsSerializer
    lookup_field = 'slug'


class CartAnimeUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartAnime.objects.all()
    serializer_class = CartAnimeUserSerializer
    permission_classes = [IsCartAnimeOwnerOrReadOnly, ]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        anime = get_object_or_404(Anime, pk=self.kwargs[self.lookup_field])
        print(self.request.authenticators)
        filter_kwargs = {'anime': anime, 'user': self.request.user}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
