from django.shortcuts import render, redirect
# CONTROLLER
# Create your views here.
def index(request):
    print request.method
    print "*"* 100
    return render(request, "first_app/index.html")

def show(request):
    print request.method
    return render(request, "first_app/show_users.html")

def create(request):
    print (request.method)
    if request.method == 'POST':
        print "*"*20
        print request.POST
        print request.method
        print "*"*20
        request.session['name'] = request.POST['first_name']
        return redirect('/')
    else:
        return redirect('/')
