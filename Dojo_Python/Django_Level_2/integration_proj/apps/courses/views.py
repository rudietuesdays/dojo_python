from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Count
from .models import Course, Description, Comment, User, UserCourse
# Create your views here.

def index(request):
    user = User.objects.get(id=request.session['uid'])
    courses = Course.objects.all()
    descriptions = Description.objects.all()
    context = {
        'courses': courses,
        'descriptions': descriptions,
        'user': user,
    }

    return render(request, "courses_templates/index.html", context)

def create(request):
    if not request.POST['name'] or not request.POST['description']:
        messages.error(request, 'Course name and description cannnot be blank')
    else:
        print request.session['uid']
        course = Course.objects.create(name=request.POST['name'], user_id=request.session['uid'])
        course_id=course.id
        description = Description.objects.create(description=request.POST['description'], course_id=course_id, user_id=request.session['uid'])
        print description

    return redirect(reverse('courses:dashboard'))

def delete_page(request, id):
    context = {
        'description': Description.objects.get(course_id=id)
    }

    return render(request, "courses_templates/delete.html", context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    Description.objects.get(course_id=id).delete()
    return redirect(reverse('courses:dashboard'))

def comment_page(request, id):
    print '*'*20
    print id
    users = User.objects.all()
    course = Course.objects.get(id=id)
    description = Description.objects.get(course_id=id)
    comments = Comment.objects.filter(course_id=id)
    context = {
        'course': course,
        'description': description,
        'comments': comments,
        'users': users,
    }
    print '*'*20
    print description.description, comments
    return render(request, "courses_templates/comments.html", context)

def commenting(request, id):
    course = Course.objects.get(id=id)
    course_id=course.id
    description = Description.objects.get(course_id=id)
    comments = Comment.objects.create(comment=request.POST['comment'], course_id=id, description_id=course_id)

    print '*'*20
    print 'redirecting to ', id
    print comments.comment
    return redirect(reverse('courses:comment_page', args=[id]))

def add_user_page(request):
    users = User.objects.all()
    courses = Course.objects.all()
    signUps = UserCourse.objects.annotate(num_users=Count('user'))
    # signUps = UserCourse.objects.filter(course__id='1').count()
    context = {
        'users': users,
        'courses': courses,
        'signUps': signUps,
    }

    return render(request, 'courses_templates/user_course.html', context)

def join_course(request):
    user = request.POST['user']
    course = request.POST['course']
    signUp = UserCourse.objects.create(user_id=user, course_id=course)
    return redirect(reverse('courses:add_user'))
