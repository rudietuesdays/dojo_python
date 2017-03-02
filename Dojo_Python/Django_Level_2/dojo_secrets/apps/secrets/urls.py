#### LOGIN AND REGISTRATION URLS ####
from django.conf.urls import url
from . import views

app_name = 'secrets'
urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^post_secret$', views.post_secret, name ='post_secret'),
    url(r'^delete_secret/(?P<id>\d+)$', views.delete_secret, name ='delete_secret'),
    url(r'^like_secret/(?P<id>\d+)$', views.like_secret, name ='like_secret'),

]
