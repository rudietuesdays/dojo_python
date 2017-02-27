from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re, bcrypt
from datetime import datetime
from ..courses.models import Course # for importing from another app, for instance to link a foreign key to another app in a manager -- only import one way! DON'T go back to the Course model and import Users -- create a third app and import there

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register_validation(self, postData):
        print 'First name: ', postData['first_name']
        messages = []

        ########## TIM'S TEACHING TIME ############
        flag = False

        # no fields can be blank
        if not postData['first_name'] or not postData['last_name'] or not postData['bday'] or not postData['password'] or not postData['confirm_password']:
            flag = True
            messages.append('No fields can be blank')

        # is email in correct format
        if not EMAIL_REGEX.match(postData['email']):
            flag = True
            messages.append('Email not valid')

        # names can only be letters
        if not NAME_REGEX.match(postData['first_name']) or not NAME_REGEX.match(postData['last_name']):
            flag = True
            messages.append('Name fields may only contain letters')

        # passwords must match
        if postData['password'] != postData['confirm_password']:
            flag = True
            messages.append('Passwords do not match')

        # password must be at least 8 characters
        if postData['password'] < 8:
            flag = True
            messages.append('Password is too short')

        # email can't already be in database
        users = Users.objects.filter(email__iexact=postData['email'])
        if users:
            flag = True
            message['unique'] = 'Your email is already in use'


        # must be at least 18 yrs old -- UNFINISHED
        try: #if u try, u must also except
            dateTimeObj = datetime.strptime(postData['bday'], '%Y-%m-%d')
            print dateTimeObj
            print datetime.now()
            flag = True
            messages.append('You must be at least 18 to register')

        except: #if try breaks AND except breaks, code will not tell you why!!
            flag = True
            messages.append('Enter a valid date')

        #if it worked!
        if not flag:
            pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

            user = User.objects.create(first_name= postData['first_name'],
            last_name=postData['last_name'], birthday=postData['bday'], email=postData['email'],
            password = pw_hash)

            return(True, user)

        else:
            return(False, messages)

        ################################

        #check if names are too short
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

    def login_validation(self, postData):
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
      email = models.EmailField(max_length=45) # EmailField will do validation for us!
      password = models.CharField(max_length=100)
      birthday = models.DateField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()
