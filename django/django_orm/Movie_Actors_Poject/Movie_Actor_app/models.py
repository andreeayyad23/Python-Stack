from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)



class Actor(models.Model):
    name = models.CharField(max_length=255)



class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url_image = models.URLField(max_length=200)
    category = models.ForeignKey(Category, related_name="movies", on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name="movies")
