from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, StarRate
User = get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'audiAcc', 'poster_url', 'description', 'genres',)

# 'description_title', 'description_subtitle', 'description_content',

class MoviesSerializer(serializers.Serializer):
    movies = MovieSerializer(many=True, required=False)
