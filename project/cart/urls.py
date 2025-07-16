from django.urls import path

from . import views

urlpatterns = [
    path('cart', views.cart, name="cart"),
    path('add_cart/<int:article>', views.add_to_cart, name="add_cart"),
    path('del_cart/<int:article>', views.del_order, name="del_cart"),
    path('del_one_cart/<int:article>', views.del_one_order, name="del_one_cart")
]
