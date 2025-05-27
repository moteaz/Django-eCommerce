from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

def store(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=Customer, complete=False)
        items = order.orderitem_set.all()
        cartIitems = order.get_cart_items
    else:
        items = []
        order = {'get_total_cart': 0, 'get_cart_items': 0}
        cartIitems = order['get_cart_items']

    Products = Product.objects.all()
    context = {'Products': Products ,'cartIitems': cartIitems}
    return render(request, 'store/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=Customer, complete=False)
        items = order.orderitem_set.all()
        cartIitems = order.get_cart_items
    else:
        items = []
        order = {'get_total_cart': 0, 'get_cart_items': 0 ,'shipping': False}
        cartIitems = order['get_cart_items']
    context={"items": items,"order": order,"cartIitems": cartIitems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        Customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=Customer, complete=False)
        items = order.orderitem_set.all()
        cartIitems = order.get_cart_items
    else:
        items = []
        order = {'get_total_cart': 0, 'get_cart_items': 0, 'shipping': False}
        cartIitems = order['get_cart_items']
    context={"items": items,"order": order,"cartIitems": cartIitems}
    return render(request, 'store/checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product ID:', productId)
    Customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=Customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse("Item was added", safe=False)