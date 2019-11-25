from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .models import Movie, Genre, Review, StarRate
# from .models import User
from .serializers import UserSerializer
User = get_user_model()
# from django.conf import settings


@api_view(['GET'])
def index(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    print(user)
    serializer = UserSerializer(instance=user)
    print(serializer)
    return Response(serializer.data)
