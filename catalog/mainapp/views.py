from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from mainapp.models import Product, Catalog

# Create your views here.


class CatalogListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'mainapp/products.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CatalogListView, self).get_context_data(*args, **kwargs)
        catalog_pk = self.kwargs.get('pk')

        if catalog_pk:
            catalog = Catalog.objects.get(id=catalog_pk)
            # print(catalog)
            context['object_list'] = Product.objects.filter(catalog=catalog)
            context['catalog_title'] = catalog.title

        else:
            context['object_list'] = Product.objects.all()
            context['catalog_title'] = 'Все категории'

        context['catalogs'] = Catalog.objects.all()
        context['catalog_pk'] = catalog_pk
        # print(type(catalog_pk))
        return context


class MainListView(ListView):
    model = Product
    queryset = Product.objects.prefetch_related('catalog')
    template_name = 'mainapp/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainListView, self).get_context_data(*args, **kwargs)
        return context
