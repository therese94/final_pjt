from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=15)
    title_en = models.CharField(max_length=30)
    audience = models.IntegerField(null=True)
    open_date = models.DateTimeField(null=True)
    genre = models.CharField(max_length=15)
    watch_grade = models.CharField(max_length=10)
    score = models.FloatField(null=True)
    poster_url = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_movies',
        )


class Comment(models.Model):
    content = models.CharField(max_length=20)
    score = models.IntegerField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)