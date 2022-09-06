from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.IntegerField()
    director = models.CharField(max_length=50)
    movie_poster = models.ImageField(upload_to='uploads/', default='')
