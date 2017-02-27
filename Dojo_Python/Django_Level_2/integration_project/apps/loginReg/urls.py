from django.conf.urls import url
from . import views

app_name = 'loginReg' #app_name variable *must* be named app_name
urlpatterns = [ # order matters! put routes first that u want checked first
    url(r'^$', views.index, name ='index'),
    url(r'^register$', views.register_user, name = 'register'),
    url(r'^login', views.login_user, name = 'login'),
    url(r'^logout', views.logout_user, name = 'logout')
]
