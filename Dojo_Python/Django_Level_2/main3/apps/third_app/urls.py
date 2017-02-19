from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blog$', views.blogs),
    url(r'^comment/(?P<id>\d+)$', views.comments)
    # url(r'^admin/', admin.site.urls),
]
