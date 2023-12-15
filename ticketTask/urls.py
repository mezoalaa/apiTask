
# urls.py
from django.contrib import admin
# from django.urls import path, include
from django.urls import path
from ticketTask import views
from .views import readCoffeeShop,addCoffeeShop,UpdateCoffee,CoffeeShopList




urlpatterns = [
    path('showcoffe/', views.CoffeeShopList.as_view(), name='show_coffee'),
    path('coffeDetails/<int:pk>/', views.readCoffeeShop.as_view(), name='coffee_details'),
    path('updateCoffe/<int:pk>/', views.UpdateCoffee.as_view(), name='update_coffee'),
    path('addcoffe/', views.addCoffeeShop.as_view(), name='add_coffee'),
]
