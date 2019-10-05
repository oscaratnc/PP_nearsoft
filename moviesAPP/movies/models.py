from django.db import models

# Create your models here.

class Artist (models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
         return self.name
     

class Movie (models.Model):
    title = models.CharField(max_length=50)
    fk_artist = models.ManyToManyField(Artist)
    def __str__(self):
        return self.title
    
