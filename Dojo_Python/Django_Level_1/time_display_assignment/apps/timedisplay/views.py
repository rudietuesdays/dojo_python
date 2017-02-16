from django.shortcuts import render, HttpResponse
import datetime
from time import strftime
now = datetime.datetime.now()
# Create your views here.
def index(request):
    print "*"*20
    print "working!"
    print "*"*20
    time_display = {
        'date': now.strftime("%A, %B %d, %Y"),
        'time': now.strftime('%I:%M %p %Z')
    }
    return render(request, 'timedisplay/index.html', time_display)
