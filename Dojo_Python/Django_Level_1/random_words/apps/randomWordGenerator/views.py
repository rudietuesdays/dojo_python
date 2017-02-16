from django.shortcuts import render, redirect
import random
import string
random_word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
# Create your views here.
def index(request):
    print '*'*20
    print request.method
    print '*'*20
    if not 'counter' in request.session:
        request.session['counter'] = 1
    word_generator = {
        'random_word': random_word,
    }
    return render(request, 'randomWordGenerator/index.html', word_generator)

def create(request):
    print '*'*20
    print request.method
    print '*'*20
    if request.method == 'POST':
        request.session['counter'] += 1
        print request.session['counter']
    return redirect('/')

def reset(request):
    print '*'*20
    print request.method
    print '*'*20
    del request.session['counter']
    return redirect('/')
