### AWESOME APP URLS ###
from django.conf.urls import url
from .views import Users, Welcome, Notes, Delete, Edit
from . import views

app_name = 'awesomeApp'
urlpatterns = [
# Your app's urls is lined to the project
    url(r'^$', Users.as_view(), name='index'),
    url(r'^notes$', Welcome.as_view(), name='dashboard'),
    url(r'^write$', Notes.as_view(), name='write'),
    url(r'^edit$', Edit.as_view(), name='edit'),
    url(r'^delete$', Delete.as_view(), name='delete'),
]
