from django.conf.urls import url
from . import views
# from django.contrib import admin

app_name = 'courses'
urlpatterns = [
    url(r'^dashboard$', views.index, name = 'dashboard'),
    url(r'^add_course$', views.create, name = 'create'),
    url(r'^delete_course/(?P<id>\d+)$', views.delete_page, name = 'delete_page'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete'),
    url(r'^comments/(?P<id>\d+)$', views.comment_page, name = 'comment_page'),
    url(r'^comment/(?P<id>\d+)$', views.commenting, name = 'commenting'),
    url(r'^sign_up$', views.add_user_page, name = 'add_user'),
    url(r'^join$', views.join_course, name = 'join_course'),
]
