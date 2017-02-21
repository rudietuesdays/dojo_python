from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.validateEmail),
    url(r'^delete/(?P<id>\d+)$', views.delete_email),
]
