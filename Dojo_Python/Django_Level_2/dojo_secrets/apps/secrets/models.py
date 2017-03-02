from __future__ import unicode_literals
from django.db import models
from ..loginReg.models import User

# Create your models here.
class SecretManager(models.Model):
    pass
    # def write_secret(self, postData):
    #     secret = Secret.objects.create(secret=postData['secret'])
    #     return (True, secret)


class Secret(models.Model):
    secret = models.TextField(max_length=255)
    user = models.ForeignKey(User, related_name='confessor')
    liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SecretManager()

class Liked(models.Model):
    secret = models.ForeignKey(Secret, related_name='confession')
    user = models.ForeignKey(User, related_name='liker')
    liked = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
