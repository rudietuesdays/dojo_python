#### USERS TO COURSES ####
from django.conf.urls import url
from . import views

app_name = 'users_courses'
urlpatterns = [
    url(r'^$', views.index, name ='index'),

]
