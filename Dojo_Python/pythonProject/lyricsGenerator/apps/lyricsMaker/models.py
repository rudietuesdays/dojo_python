from __future__ import unicode_literals
from django.db import models
# from django.forms import ModelForm

# Create your models here.

class SongManager(models.Manager):
    pass

class Song(models.Model):
    genre = models.CharField(max_length=45)
    subj = models.CharField(max_length=45)
    pronouns = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SongManager()
