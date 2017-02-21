from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.CharField(max_length=45)
    date_added = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
