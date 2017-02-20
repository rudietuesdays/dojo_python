from django.shortcuts import render, redirect
from .models import Course, Description, Comment
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
    course = Course.objects.create(name=request.POST['name'])
    course_id=course.id
    description = Description.objects.create(description=request.POST['description'], course_id=course_id)
    print description

    return redirect('/')

def delete_page(request, id):
    context = {
        'description': Description.objects.get(course_id=id)
    }

    return render(request, "courses/delete_course.html", context)

def delete(request, id):
    Description.objects.get(course_id=id).delete()
    return redirect('/')

def comment_page(request, id):
    course = Course.objects.get(id=id)
    description = Description.objects.get(course_id=id)
    comments = Comment.objects.filter(course_id=id)
    context = {
        'course': course,
        'description': description,
        'comments': comments,
    }
    print description.description, comments
    return render(request, "courses/comments.html", context)

def commenting(request, id):
    course = Course.objects.get(id=id)
    course_id=course.id
    description = Description.objects.get(course_id=id)
    comments = Comment.objects.create(comment=request.POST['comment'], course_id=id, description_id=course_id)
    
    print '*'*20
    print 'redirecting to ', id
    print comments.comment
    return redirect('/comments/{}'.format(id))
