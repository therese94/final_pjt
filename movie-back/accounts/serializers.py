from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Genre, StarRate, Review
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'followers', 'favorite_genres', 'potential_movies', 'reviews',)
