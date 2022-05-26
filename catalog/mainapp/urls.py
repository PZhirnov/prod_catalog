from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('test/', mainapp.test, name='index'),
    path('', mainapp.ProductsListView.as_view(), name='products'),
]
