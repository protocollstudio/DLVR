from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=250)
    path = models.CharField(max_length=250, null=True, blank=True)
    artwork = models.ImageField(null=True, blank=True)
    audio_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title
