from django.db import models
from django.contrib.auth.models import User



TYPES = (
    ('Film', 'Film'),
    ('TV Show', 'TV Show')
)

RATING_CHOICES = (
    (1, '1 - Poor'),
    (2, '2 - Fair'),
    (3, '3 - Good'),
    (4, '4 - Very Good'),
    (5, '5 - Excellent'),
)


class Media(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    poster = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255)
    type = models.CharField(
        max_length=10,
        choices=TYPES,
    )
    is_viewed = models.BooleanField()
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        null=True,  
        blank=True,  
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} ({'Viewed' if self.is_viewed else 'Not Viewed'})"
