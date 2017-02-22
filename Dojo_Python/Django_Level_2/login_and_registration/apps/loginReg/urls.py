from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register_user),
    url(r'^login', views.login_user),
    url(r'^logout', views.logout_user)
]
