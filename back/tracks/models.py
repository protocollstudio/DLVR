from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=250)
    path = models.CharField(max_length=250)
    artwork = models.ImageField()

    def __str__(self):
        return self.title
