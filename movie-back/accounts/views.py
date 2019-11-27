from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.models import Movie
from .serializers import UserSerializer
User = get_user_model()

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8080/')
        # 회원가입 로직
        
    else:   # GET
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@api_view(['GET'])
def index(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    print(user)
    serializer = UserSerializer(instance=user)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def potential(request, user_id, movie_id):
    user = get_object_or_404(User, pk=user_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    if user.potential_movies.filter(pk=movie_id).exists(): # 1개의 데이터라도 존재하면 True
        user.potential_movies.remove(movie)
    else:
        user.potential_movies.add(movie)
    # user.
    print(user.pk)
    print(movie.title)
    # print(user.potential_movies)
    return Response('message')


@api_view(['POST'])
def follow(request, user_id, following_id):
    user = get_object_or_404(User, pk=user_id)
    following_user = get_object_or_404(User, pk=following_id)
    if user.followers.filter(pk=following_id).exists(): # 1개의 데이터라도 존재하면 True
        user.followers.remove(following_user)
    else:
        user.followers.add(following_user)
    serializer = UserSerializer(instance=following_user)
    return Response(serializer.data)