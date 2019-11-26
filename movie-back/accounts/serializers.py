from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Genre, StarRate, Review
User = get_user_model()
# from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'followers', 'favorite_genres', 'potential_movies', 'reviews',)
