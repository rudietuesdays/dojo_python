from __future__ import unicode_literals
from django.db import models
import re

INT_RE = re.compile(r'^[0-9]+$')

# Create your models here.

class ProductManager(models.Manager):
    def validate(self, postData):
        messages = []
        flag = False

        if not postData['name'] or not postData['description'] or not  postData['price']:
            flag = True
            messages.append('No field may be blank')

        if not INT_RE.match(postData['price']):
            flag = True
            messages.append('Price may only contain numbers')

        if not flag:
            if Product.objects.filter(id=postData['id']).exists():
                product = Product.objects.get(id=postData['id'])
                product.name = postData['name']
                product.description = postData['description']
                product.price = postData['price']
                product.save()
                return (True, product)
            else:
                products = Product.objects.create(name=postData['name'], description= postData['description'], price=postData['price'])
                return (True, products)
        else:
            return (False, messages)

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
