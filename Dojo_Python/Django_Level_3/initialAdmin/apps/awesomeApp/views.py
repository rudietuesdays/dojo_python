from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm, NoteForm
from .models import Note
from django.views.generic import View
from django.http import HttpResponse

class Users(View):
    def get(self, request):
        regForm = RegisterForm()

        context = {
            "regForm": regForm,
            }
        return render(request, "awesomeApp_templates/index.html", context)

    def post(self, request):
        # Confirm that the HTTP verb was a POST
        # Bind the POST data to an instance of our RegisterForm
        bound_form = RegisterForm(request.POST)
        # Now test that bound_form using built-in methods!
        # *************************
        print bound_form.is_valid() # True or False, based on the validations that were set!
        print bound_form.errors # Any errors in this form as a dictionary
        # *************************
        return HttpResponse('thank you')

class Welcome(View):
    def get(self, request):
        notes = Note.objects.all()
        new_note_form = NoteForm()

        # print notes

        context = {
            'notes': notes,
            'new_note_form': new_note_form,
        }

        return render(request, "awesomeApp_templates/notes.html", context)

class Notes(View):
    def get(self, request):
        context = {
            'notes': Note.objects.all(),
        }
        return render(request, 'awesomeApp_templates/div.html', context)
    def post(self, request):
        bound_form = NoteForm(request.POST)
        if bound_form.is_valid():
            Note.objects.create(note=request.POST['note'])
        return redirect(reverse('awesomeApp:write'))

class Edit(View):
    def get(request):
        print 'editing...'
        Note.object.
        return redirect(reverse('awesomeApp:dashboard'))
    def post(request):

        return (redirect(reverse('awesomeApp:edit')))

class Delete(View):
    def post(self, request):
        print 'deleting...'
        id = request.POST['Delete']
        print id
        note = Note.objects.get(id=id)
        note.delete()
        return (redirect(reverse('awesomeApp:dashboard')))
