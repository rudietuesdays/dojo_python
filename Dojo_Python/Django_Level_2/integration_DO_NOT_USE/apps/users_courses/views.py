#### USERS TO COURSES ####
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'users_courses/index.html')
