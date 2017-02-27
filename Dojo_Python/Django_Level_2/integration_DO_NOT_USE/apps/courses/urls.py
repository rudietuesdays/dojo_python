#### COURSES APP ####
from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^courses$', views.index, name ='index'),
    url(r'^add_course$', views.create, name='create'),
    url(r'^delete_course/(?P<id>\d+)$', views.delete_page, name='delete_page'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^comments/(?P<id>\d+)$', views.comment_page, name = 'comment_page'),
    url(r'^comment/(?P<id>\d+)$', views.commenting, name='commenting'),
]
