from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comment
# Create your views here.

def index(request):
    context = {
        'blogs': Post.objects.all()
        # SELECT * FROM Post
    }
    return render(request, "third_app/index.html", context)

    # print(User.objects.all())
    # # A list of objects (or an empty list)
    # User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
    # # Creates a user object
    # print(User.objects.all())
    # # A list of objects (or an empty list)
    # u = User.objects.get(id=1)
    # print(u.first_name)
    # u.first_name = "Joey"
    # u.save()
    # j = User.objects.get(id=1)
    # print(j.first_name)
    # # Gets the user with an id of 1, changes name and saves to DB, then retrieves again...
    # print(User.objects.get(first_name=u.first_name))
    # # Gets the user with a first_name of 'mike' *** THIS MIGHT NEED TO BE CHANGED ***
    # users = User.objects.raw("SELECT * from third_app_user")
    # # Uses raw SQL query to grab all users (equivalent to User.objects.all()), which we iterate through below
    # for user in users:
    #     print user.first_name
    #     print User._meta.db_table
    # return HttpResponse("ok")

def blogs(request):
    #using ORM
    Post.objects.create(title=request.POST['title'], message=request.POST['blog'])
    #insert into post (title, blog, created, updated at) values (title, post, now(), now())
    return redirect('/')

def comments(request, id):
    blog = Post.objects.get(id=id)
    print blog.id
    Comment.objects.create(comment = request.POST['comment'], post_id=blog.id)
    return redirect('/')
