from django.conf.urls import url
from views import Welcome, Songs

app_name = 'lyricsMaker'

urlpatterns = [
    url(r'^$', Welcome.as_view(), name='index'),
    url(r'song$', Songs.as_view(), name='song'),
]
