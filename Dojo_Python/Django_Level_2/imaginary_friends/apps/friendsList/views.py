from django.shortcuts import render, redirect
from .models import Friend, Friendship

# Create your views here.
def index(request):
    context = {
        'friends': Friend.objects.all(),
        'friendships': Friendship.objects.all()
    }
    print Friendship.objects.all()
    return render(request, 'friendsList/index.html', context)

def add_friend(request):
    friends = Friend.objects.create(name=request.POST['name'])
    print friends

    return redirect('/')

def join_friends(request):
    friend_1 = request.POST['friend_1']
    friend_2 = request.POST['friend_2']
    friendship = Friendship.objects.create(friend_1_id=friend_1, friend_2_id=friend_2)
    print friend_1
    print friend_2
    print friendship
    return redirect('/')
