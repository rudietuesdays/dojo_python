from __future__ import unicode_literals
from django.db import models
from ..loginReg.models import User

# Create your models here.

#would need 2 manager classes for Course and Description
# class CourseManager(models.Manager):
#     def validate_course(self, postData):
#         messages = []
#
#         if not postData['name'] or not postData['description']:
#             messages.append('Course name and description cannnot be blank')
#             return(False, messages)
#
#         else:
#             course = Course.objects.create(name=request.POST['name'])
#             description = Description.objects.create(description=request.POST['description'], course_id=course_id)
#             return (True, course, description)

class Course(models.Model):
    name = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name='creator')
    date_added = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Description(models.Model):
    description = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, related_name='course_description')
    user = models.ForeignKey(User, related_name='writer')
    date_added = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User, related_name='commentator')
    description = models.ForeignKey(Description)
    date_added = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class UserCourse(models.Model):
    user = models.ForeignKey(User, related_name='users')
    course = models.ForeignKey(Course, related_name='courses')
