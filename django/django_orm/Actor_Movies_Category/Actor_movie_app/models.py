from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def movie_count(self):
        return self.movies.count()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url_image = models.URLField(max_length=200)
    category = models.ForeignKey(Category, related_name="movies", on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title
    
    