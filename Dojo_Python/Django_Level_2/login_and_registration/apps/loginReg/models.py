from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+[^0-9]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, postData):
        print 'First name: ', postData['first_name']
        messages = []

        if (len(postData['first_name']) < 2) and (len(postData['last_name']) < 2):
            messages.append('First and last name must be longer than two characters')
        elif (not NAME_REGEX.match(postData['first_name'])) and (not NAME_REGEX.match(postData['last_name'])):
            messages.append('Name cannot contain numbers or special characters')
        if not EMAIL_REGEX.match(postData['email']):
            messages.append('Please enter a valid email address')
        if (len(postData['password']) < 7):
            messages.append('Password must be at least 8 characters long')
        elif not postData['password'] == postData['confirm_pw']:
            messages.append('Passwords must match')

        if len(messages) != 0:
            return (False, messages)

        else:
            pw_hash = bcrypt.hashpw(str(postData['password']), bcrypt.gensalt())

            user = User.objects.create(first_name= postData['first_name'],
            last_name=postData['last_name'], email=postData['email'],
            password = pw_hash)
            return (True, user)

    def login(self, postData):
        messages = []
        flag = False
        if len(postData['email']) < 1:
            flag = True
            messages.append('Please enter your email address')

        if len(postData['email']) > 0:
            user = User.objects.filter(email=postData['email'])

            if len(user) < 1:
                flag = True
                messages.append('Email not found')
                print 'this is the user: ', user
        else:
            user = False

        if len(postData['password']) < 1:
            flag = True
            messages.append('Password too short')

        if user:
            print "bcrypt result"
            print (bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) == user[0].password)

            if not bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) == user[0].password:
                flag = True
                messages.append('Password is not valid')

        print "here"
        print flag

        if flag:
            return (False, messages)
        else:
            return (True, user)


    def name(self, email):
        pass



    def validate_pw(self, postData):
        pass

class User(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      email = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()
