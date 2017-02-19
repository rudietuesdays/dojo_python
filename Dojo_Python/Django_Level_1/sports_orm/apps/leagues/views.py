from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	baseball = League.objects.filter(sport__contains="baseball")
	women = League.objects.filter(name__contains="women")
	hockey = League.objects.filter(sport__contains='hockey')
	not_football = League.objects.exclude(sport__contains="football")
	conferences = League.objects.filter(name__contains='conference')
	atlantic = League.objects.filter(name__contains='atlantic')
	dallas = Team.objects.filter(location__contains='dallas')
	raptors = Team.objects.filter(team_name__contains='raptors')
	city = Team.objects.filter(location__contains='city')
	t_name = Team.objects.filter(team_name__startswith='t')
	azLocation = Team.objects.order_by('location')
	zaLocation = Team.objects.order_by('-location')
	cooper = Player.objects.filter(last_name__contains='cooper')
	joshua = Player.objects.filter(first_name__contains='joshua')
	coopNotJosh = Player.objects.filter(last_name__contains='cooper').exclude(first_name__contains='joshua')
	alexOrWyatt = Player.objects.filter(first_name__contains='alex')|Player.objects.filter(first_name__contains='wyatt')

	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": alexOrWyatt, # Player.objects.all(),
	}




	print baseball

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
