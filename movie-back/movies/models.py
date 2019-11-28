from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=30)
    audiAcc = models.IntegerField()
    audiRating = models.FloatField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genres = models.TextField()


class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

class StarRate(models.Model):
    num_star = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='star_rates')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)