from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	#sports ORM queries
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
	#sports ORM continued queries
	atlanticConf =  League.objects.filter(name__contains='Atlantic Soccer Conference')
	atlanticTeams = Team.objects.filter(league=atlanticConf)
	penguins = Team.objects.filter(team_name__contains='Penguins')
	penguinsCurrent = Player.objects.filter(curr_team=penguins)
	icbc = League.objects.filter(name='International Collegiate Baseball Conference')
	icbcTeam = Team.objects.filter(league=icbc)
	icbcCurrent = Player.objects.filter(curr_team=icbcTeam)
	acaf = League.objects.filter(name='American Conference of Amateur Football')
	acafTeam = Team.objects.filter(league=acaf)
	acafHernandez = Player.objects.filter(curr_team=acafTeam).filter(last_name='Hernandez')
	football = League.objects.filter(sport__contains='Football')
	footballTeam = Team.objects.filter(league=football)
	footballPlayers = Player.objects.filter(all_teams=footballTeam)
	sophiaTeam = Team.objects.filter(curr_players__first_name='Sophia')
	sophiaLeague = League.objects.filter(teams__curr_players__first_name='Sophia')
	notFlores = Player.objects.exclude(curr_team__team_name__icontains='rough').filter(last_name='Flores')
	evans = Team.objects.filter(all_players__first_name="Samuel").filter(all_players__last_name='Evans')
	tigerCats = Player.objects.filter(all_teams__team_name__icontains='tiger-cats')
	vikings = Player.objects.filter(all_teams__team_name__icontains='vikings').exclude(curr_team__team_name__icontains='vikings')
	jacobNotColts = Team.objects.exclude(team_name__contains='Colts').filter(all_players__first_name='Jacob').filter(all_players__last_name='Gray')
	joshBaseball = Player.objects.filter(first_name='Joshua').filter(all_teams__league__name__contains='amateur baseball')
	# numPlayers = count(Player.objects.all())
	# dozenPlus = Team.objects.annotate(
	# 	numPLayers = Case(
	# 		When(numPlayers > 12)
	# 		)
	# 	)

	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}

	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
