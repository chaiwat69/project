import datetime
from itertools import product
#from operator import div
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def list_product(request):
    text ="""
         <ul>
    """
    for i in Product.objects.all():
        text =text+'<li>'+str(i.name)+ str(i.price) +' ฿ </li>'
        return HttpResponse(text)

def product_list(request):
        querysets = Product.objects.all()
        return render(request, 'product_list.html', {'qs': querysets})

def index(request):
        querysets = Product.objects.all()
        return render(request, 'index.html', {'qs': querysets})

