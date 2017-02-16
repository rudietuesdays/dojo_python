# print "I will be your future routes; HTTP requests will be captured by me."

#

from django.conf.urls import url #This gives us access to the variable url (which points to a function)
from . import views #This gives us access to everything in a views.py file that Django automatically created for us when we built our first_app (from whereever you are, import views)

# the url method is used similarly to @app.route in Flask
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.show),
    url(r'^new_user', views.create)
]

# def method_to_run(request):
#       print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
#       print "By the way, here's the request object that Django automatically passes us:", request
#       print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
#
# urlpatterns = [
#     url(r'^$', method_to_run),
# ]
