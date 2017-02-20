from django.shortcuts import render, redirect
from django.contrib import messages
import re, datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.

def index(request):
    if 'random' not in request.session:
        request.session['random']= 'necessary'
    if 'email' not in request.session:
        request.session['email']=[]
    print '*'*20
    print request.session['email']

    return render(request, 'emailValidation/index.html')

def validateEmail( request ):
    emails = request.POST['email']
    timestamp = '{:(%Y/%m/%d %H:%M%p)}'.format(datetime.datetime.now())

    if EMAIL_REGEX.match(request.POST['email']):
        messages.success(request, ('The email address you entered, {}, is valid. Thanks for submitting your info to the overlords!').format(request.POST['email']))
        context = {
            'emails': emails,
            'timestamp': timestamp,
        }

        request.session['email'].insert(0, context)
        request.session['random']='this exists'
    else:
        messages.warning(request, 'The email address you entered is not valid! Please try again.')

    # emails.append(request.POST['email'])
    # request.session['email'] = emails




    print '*'*20
    print request.session['email'], timestamp
    print '*'*20
    # Try it with django's email validator:
    # from django.core.validators import validate_email
    # from django.core.exceptions import ValidationError
    # try:
    #     validate_email( request.POST['email'] )
    #     return True
    # except ValidationError:
    #     return False

    return redirect('/')

def delete_email(request, email):
    request.session.modified = True


    return redirect('/')
