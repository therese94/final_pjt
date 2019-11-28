from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Movie


# User 모델을 Customizing 한다.
# default user model을 사용하더라도 확장성을 위해서 customizing 한다.
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'follwings'      # 역참조를 위해서 필요한것
    )
    # favorite_genres = models.ManyToManyField(Genre, related_name='genre_liked_users')
    potential_movies = models.ManyToManyField(Movie, related_name='potential_audis')