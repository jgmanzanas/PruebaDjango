from django.urls import path

from . import views

urlpatterns = [
    path('price', views.orderpricedesc, name='orderpricedesc'),
    path('discount', views.orderdiscountdesc, name='orderdiscountdesc'),
    path('comedy', views.getcomedy, name='getcomedy'),
]