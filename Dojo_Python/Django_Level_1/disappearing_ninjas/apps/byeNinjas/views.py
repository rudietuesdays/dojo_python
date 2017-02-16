from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    return render(request, "byeNinjas/index.html")

def show(request):
    context = {
        'all_ninjas': True,
    }
    print "*"*20
    print 'all the ninjas'
    print "*"*20
    return render(request, "byeNinjas/ninjas.html", context)

def ninja(request, color):
    context = {
        'color': color,
    }
    print "*"*20
    print color
    print "*"*20
    return render(request, 'byeNinjas/ninjas.html', context)
