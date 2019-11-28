from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, StarRate, Review
User = get_user_model()
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'audiAcc', 'poster_url', 'description', 'genres', 'reviews',)
class MoviesSerializer(serializers.Serializer):
    movies = MovieSerializer(many=True, required=False)
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'score', 'content', 'user', 'movie',)