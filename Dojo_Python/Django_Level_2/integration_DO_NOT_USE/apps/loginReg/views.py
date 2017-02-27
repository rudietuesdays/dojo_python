from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'uid' not in request.session:
        request.session['uid'] = ''
        print 'ID:', request.session['uid']

    print '*'*20
    print 'All users:', User.objects.all()
    # print 'Most recent registration:', User.objects.last(first_name)
    return render(request, 'loginReg/index.html')

def register_user(request):
    postData = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_pw': request.POST['confirm_pw'],
    }

    #pull register method from models.py
    result = User.objects.register_validation(postData)

    #check true or false : user[0] is True, user[1] is false , which comes from the tuple in models.py
    if result[0]:
        print '*'*20
        print result[0], result[1]
        request.session['uid'] = result[1].id
        # user_obj = result[1]
        #
        # context = {
        #     'user_obj': user_obj
        # }

        return redirect('/courses')

    #loop through messages showing errors if the registration wasn't successful
    else:
        for err in range(len(result[1])):
            messages.error(request, result[1][err])
        return redirect('/')

def login_user(request):

    postData = {
        'email': request.POST['login_email'],
        'password': request.POST['login_password'],
    }

    user = User.objects.login_validation(postData)

    print '*'*20
    print user[1]
    if user[0]:
        request.session['uid'] = user[1][0].id
        user_obj = user[1][0]
        context = {
            "user_obj": user_obj
        }
        return redirect('/courses')
    else:
        for message in range(len(user[1])):
            messages.error(request, user[1][message])
        return redirect('/')

def display_courses(request):
    context = {
        "user": User.objects.get(id=request.session['uid']),
        # 'courses': Course.objects.all(),
        # 'descriptions': Description.objects.all()
    }

    return render(request, 'courses/index.html', context) #redirect from here to a html page from courses app, and render the page in there?

def logout_user(request):
    del request.session['uid']
    return redirect('/')
