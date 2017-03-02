from django import forms
from .models import User, Note
# from django.db import models

# class RegisterForm(forms.Form):
#     first_name = forms.CharField(max_length=45)
#     last_name = forms.CharField(max_length=45)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']
    def save(self, commit=True):
        note = super(NoteForm, self).save(commit=False)
        note.note = self.cleaned_data['note']
        if commit:
            note.save()
        return note    
