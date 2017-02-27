from __future__ import unicode_literals
from django.db import models
from ..courses.models import Course, Description, Comment
from ..loginReg.models import User

# Create your models here.

class UserCourse(models.Model):
    user = models.ManyToManyField(User, related_name=
    'course_user')
    course = models.ManyToManyField(Course, related_name='user_course')
    description = models.ForeignKey(Description, related_name='course_description')
    comment = models.ForeignKey(Comment, related_name='course_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
