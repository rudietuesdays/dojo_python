from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .models import Song


# Create your views here.
class Welcome(View):
    def get(self, request):
        songs = Song.objects.all()

        print songs

        return render(request, 'lyricsMaker_templates/index.html')

    def post(self, request):
        genre = request.POST['genre']
        subj = request.POST['subject']
        pronouns = request.POST['pronouns']

        write_song = Song.objects.create(genre=genre, subj=subj, pronouns=pronouns)

        print genre, subj, pronouns

        return redirect('/song')

class Songs(View):
    def get(self, request):
        song = Song.objects.get(id=1)

        context = {
            'song': song,
        }
        return render(request, 'lyricsMaker_templates/lyrics.html', context)
    def post(self, request):
        song = Song.objects.get(id=1)

        context = {
            'song': song,
        }
        return render(request, 'lyricsMaker_templates/lyrics.html', context)
