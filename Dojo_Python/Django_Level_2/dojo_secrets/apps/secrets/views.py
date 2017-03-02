from django.shortcuts import render, redirect, reverse
from .models import User, Secret, Liked

# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['uid'])
    secrets = Secret.objects.all()
    likedSecret = Liked.objects.all() #
    print likedSecret[0].secret.id

    for secret in secrets:
        if not secret.Liked_set.all().exists:
            liked = False
        else:
            liked = True
        #
        # likedThis = likedSecret.filter(secret_id=secret.id).filter(user_id=user.id)
        # if likedThis.exists():
        #     liked = True
        #     print likedThis[0].secret.secret
        # else:
        #     liked = False

    context = {
        'user': user,
        'secrets': secrets,
        'likedSecret': likedSecret,
        'liked': liked,
    }
    return render(request, 'secrets_templates/index.html', context)

def post_secret(request):
    user = User.objects.get(id = request.session['uid'])
    user_id = user.id
    secret = Secret.objects.create(secret=request.POST['secret'], user_id=user_id)

    return redirect(reverse('secrets:index'))

def delete_secret(request, id):
    secret = Secret.objects.get(id=id)
    secret.delete()
    return redirect(reverse('secrets:index'))

def like_secret(request, id):
    secret = Secret.objects.get(id=id)
    user = User.objects.get(id=request.session['uid'])
    liked =  Liked.objects.create(secret_id=secret.id, user_id=user.id)

    return redirect(reverse('secrets:index'))
