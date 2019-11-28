from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Movie

class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name = 'follwings'
    )
    potential_movies = models.ManyToManyField(Movie, related_name='potential_audis')