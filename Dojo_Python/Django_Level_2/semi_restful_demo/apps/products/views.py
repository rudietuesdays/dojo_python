from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    print products
    context = {
        'products': products,
    }

    return render(request, 'products_templates/index.html', context)

def new(request):
    return render(request, 'products_templates/new.html')

def create(request):
    postData = {
        'id': False,
        'name': request.POST['name'],
        'description': request.POST['description'],
        'price': request.POST['price'],
    }

    result = Product.objects.validate(postData)

    if result[0]:
        return redirect(reverse('products:index'))
    else:
        for err in range(len(result[1])):
            messages.error(request, result[1][err])
        return redirect(reverse('products:new'))

def show(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product,
    }
    return render(request, 'products_templates/show.html', context)

def edit(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product,
    }
    return render(request, 'products_templates/edit.html', context)

def update(request, id):
    postData = {
        'id': id,
        'name': request.POST['name'],
        'description': request.POST['description'],
        'price': request.POST['price'],
    }

    result = Product.objects.validate(postData)

    if result[0]:
        return redirect(reverse('products:show', args=[id]))
    else:
        for err in range(len(result[1])):
            messages.error(request, result[1][err])
        return redirect(reverse('products:edit', args=[id]))

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(reverse('products:index'))
