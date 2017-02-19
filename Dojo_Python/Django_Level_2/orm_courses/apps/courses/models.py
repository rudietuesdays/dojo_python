from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=45)
    date_added = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Description(models.Model):
    description = models.TextField(max_length=1000)
    course = models.ForeignKey(Course)
    date_added = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
