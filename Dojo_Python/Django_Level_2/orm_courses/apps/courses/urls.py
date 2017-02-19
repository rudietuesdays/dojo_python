from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.create),
    url(r'^delete_course/(?P<id>\d+)$', views.delete_page),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]
