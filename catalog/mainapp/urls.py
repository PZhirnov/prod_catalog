from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('catalogs/', mainapp.CatalogListView.as_view(), name='catalogs'),
    path('catalogs/<int:pk>/', mainapp.CatalogListView.as_view(), name='catalogs'),
    path('', mainapp.MainListView.as_view(), name='index'),
    path('index/', mainapp.MainListView.as_view(), name='index'),
]
