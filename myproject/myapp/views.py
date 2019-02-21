import datetime
from itertools import product
#from operator import div
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.views import generic


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def product_list(request):
        querysets = Product.objects.all()
        return render(request, 'product_list.html', {'qs': querysets})

def index(request):
        querysets = Product.objects.all()
        return render(request, 'index.html', {'qs': querysets})

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list2.html'
    #queryset = Product.objects.filter(category='V')
    queryset = Product.objects.all()
    # paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['name'] = 'Hey Wasit!!'
        
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Hey Wasit!!'
        return context