from django.shortcuts import render, redirect
from .models import Course, Description
# Create your views here.

def index(request):
    courses = Course.objects.all()
    descriptions = Description.objects.all()
    context = {
        'courses': courses,
        'descriptions': descriptions
    }
    print context['courses'], context['descriptions']
    return render(request, "courses/index.html", context)

def create(request):
    # course = Course.objects.get(id=id)
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    # Description.objects.create(description=request.POST['description'], course_id=course.id)

    return redirect('/')

def delete_page(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }

    return render(request, "courses/delete_course.html", context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
