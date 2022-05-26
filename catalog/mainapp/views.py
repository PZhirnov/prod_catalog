from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from mainapp.models import Product

# Create your views here.

def test(request):
    return HttpResponse("Here's the text of the web page.")


class ProductsLIstView(ListView):
    model = Product
    template_name = 'mainapp/products.html'