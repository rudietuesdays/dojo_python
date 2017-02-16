from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print "*"*20
    print request.method
    print "*"*20
    return render(request, "surveyForm/index.html")

def create(request):
    print "*"*20
    print request.method
    print "*"*20
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    return redirect('/result')

def process(request):
    print "*"*20
    print request.method
    print "*"*20
    return render(request, 'surveyForm/result.html')

def redirecting(request):
    print "*"*20
    print request.method
    print "*"*20
    return redirect('/')
