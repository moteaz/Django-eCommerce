from django.shortcuts import render
from .models import *

def store(request):
    Products = Product.objects.all()
    context = {'Products': Products}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=Customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_cart': 0, 'get_cart_items': 0}
    context={"items": items,"order": order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=Customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_cart': 0, 'get_cart_items': 0}
    context = {"items": items, "order": order}
    return render(request, 'store/checkout.html', context)