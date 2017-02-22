from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=45)
    date_added = models.DateTimeField(auto_now_add=True)

class Friendship(models.Model):
    friend_1 = models.ForeignKey(Friend, related_name='friend_1')
    friend_2 = models.ForeignKey(Friend, related_name='friend_2')
