from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length= 255)
    artist = models.CharField(max_length= 255)
    album = models.CharField(max_length= 255)
    release_date = models.DateField(blank = True)
    genre = models.CharField(max_length= 255)