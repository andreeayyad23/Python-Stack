from copy import error
import datetime
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title cannot be less than 2 characters!"
        else:
            try:
                show = Show.objects.get(title__iexact=postData['title'])
                errors['title'] = "is taken please try another one"
            except:
                pass

        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"

        if 0 < len(postData['description']) and  len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"

        if len(postData['release_date']) > 0:
            _releaseDate = datetime.datetime.strptime(
                postData['release_date'], '%Y-%m-%d')
            _todayDate = datetime.datetime.today()
            if _todayDate < _releaseDate:
                errors['release_date'] = "date should be in the past!"
        else:
            errors['release_date'] = "Field is required!"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    description = models.TextField(default="No description is set.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= ShowManager()