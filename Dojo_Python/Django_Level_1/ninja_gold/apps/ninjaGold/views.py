from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'activities' in request.session:
        request.session['activities'] = []
    print "*"*20
    print request.session['gold'], request.session['activities']
    print "*"*20
    return render(request, "ninjaGold/index.html")

def find_gold(request):
    color = 'green'
    log = 'win'
    if request.POST['building'] == 'farm':
        new_gold = random.randrange(10, 21)
        print "*"*20
        print 'farm gold:', new_gold, 'total gold:', request.session['gold']
        print "*"*20
    if request.POST['building'] == 'cave':
        new_gold = random.randrange(5, 11)
        print "*"*20
        print 'cave gold:', new_gold, 'total gold:', request.session['gold']
        print "*"*20
    if request.POST['building'] == 'house':
        new_gold = random.randrange(2, 6)
        print "*"*20
        print 'house gold:', new_gold, 'total gold:', request.session['gold']
        print "*"*20
    if request.POST['building'] == 'casino':
        new_gold = random.randrange(-50, 51)
        print "*"*20
        if new_gold < 0:
            color = 'red'
            log = "lost"

    timestamp = '{:(%Y/%m/%d %H:%M%p)}'.format(datetime.datetime.now())
    if log != "lost":
        log = "Earned {} gold from the {}! ... ".format(new_gold, request.POST['building']) + timestamp
    else:
        log = "Lost {} gold from the {}! Ouch ... ".format(new_gold, request.POST['building']) + timestamp
    print "*"*20
    print log
    print "*"*20

    data = {
        'log': log,
        'color': color
    }

    request.session['activities'].insert(0, data)
    request.session['gold'] += new_gold

    return redirect('/')

def start_over(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')
