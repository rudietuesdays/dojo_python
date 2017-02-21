from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.

def index(request):
    emails = Email.objects.all()

    context = {
        'emails': emails,
    }

    print '*'*20
    print emails

    return render(request, 'emailsWithDb/index.html', context)

def validateEmail( request ):
    emails = Email.objects.create(email=request.POST['email'])

    if EMAIL_REGEX.match(request.POST['email']):
        messages.success(request, ('The email address you entered, {}, is valid. Thanks for submitting your info to the overlords!').format(request.POST['email']))
        context = {
            'emails': emails,
        }

        # request.session['email'].insert(0, context)
        # request.session['random']='this exists'
    else:
        messages.warning(request, 'The email address you entered is not valid! Please try again.')

    print '*'*20
    print emails
    print '*'*20

    return redirect('/')

def delete_email(request, id):
    # email = Email.objects.get(id=id)
    # email_id = email.id
    # email.delete()
    Email.objects.get(id=id).delete()

    return redirect('/')
