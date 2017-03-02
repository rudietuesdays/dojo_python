from __future__ import unicode_literals
from django.db import models
from django import forms

# Create your models here.

# def validateLengthGreaterThanTwo(value):
#     if len(value)< 3:
#         raise ValidationError('{} must be longer than: 2'.format(value))

class User(models.Model):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)

    def __str__(self):
        return (self.first_name, self.last_name, self.email, self.password, self.confirm_password)


class U(models.Model):
    pass

class Fruit(models.Model):
    pass

class Donut(models.Model):
    pass

class Group(models.Model):
    pass

class Note(models.Model):
    note = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note
