from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Genre, Review
from .serializers import MovieSerializer, MoviesSerializer
User = get_user_model()



@api_view(['GET'])
def index(request):
    movies = get_list_or_404(Movie)
    for a in movies:
        print(a)
    # print(movies)
    serializers = MoviesSerializer(instance=movies)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save()
    return Response(serializers.data)
