from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer

from api.serializers import CartAnimeForProfileSerializer

User = get_user_model()


class ExtUserSerializer(UserSerializer):
    class Meta(UserSerializer):
        model = User
        fields = (
            'avatar',
            'nickname',
            'username'
        )


class UserProfileSerializer(UserSerializer):
    cart_anime = CartAnimeForProfileSerializer(many=True)

    class Meta(UserSerializer):
        model = User
        fields = (
            'nickname',
            'avatar',
            'about',
            'cart_anime',
            'username'
        )
