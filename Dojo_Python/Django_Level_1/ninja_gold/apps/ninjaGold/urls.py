from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money', views.find_gold),
    url(r'^replay', views.start_over)
]
