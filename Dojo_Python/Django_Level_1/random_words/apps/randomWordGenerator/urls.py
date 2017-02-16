from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_word', views.create),
    url(r'^reset_count', views.reset ),
]
