from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey_process', views.create),
    url(r'^result', views.process),
    url(r'^redirect_home', views.redirecting),
]
