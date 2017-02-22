from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add_friend),
    url(r'^join$', views.join_friends),
]
