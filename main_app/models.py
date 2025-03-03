from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10)  

    def __str__(self):
        return f"{self.title} ({self.release_year})"
