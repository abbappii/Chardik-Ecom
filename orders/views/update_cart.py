from products.database.products import Products
from django.shortcuts import get_object_or_404
from orders.database.cart import Cart 
from orders.database.order import Order
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view


'''
Remove Item from Cart
Increase Item in Cart
Decrease Item in Cart
'''

# Remove item from cart
@api_view(['GET','POST'])
def remove_from_cart(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_table =  Order.objects.filter( user= request.user, ordered=False)

    if order_table.exists():
        order = order_table[0]
        if order.orderItems.filter(item=item).exists():
            cart_check = Cart.objects.filter(item=item,user=request.user, purchased=False)[0]
            order.orderItems.remove(cart_check)
            cart_check.delete()
            return Response({})
            #return redirect('Order:cartView')
        else:
            return Response({})
            #return redirect('Products:index')

    else:
        #return Response({})
        return redirect('Products:index')



#Increase Item from Cart
@api_view(['GET','POST'])
def increase_item(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_table = Order.objects.filter(user=request.user, ordered=False)

    if order_table.exists():
        order = order_table[0]
        if order.orderItems.filter(item=item).exists():
            cart_check = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if cart_check.quantity>=1:
                 cart_check.quantity+=1
                 cart_check.save()
                 return Response({})
                 #return redirect('Order:cartView')
        else:
            return Response({})
            #return redirect('Products:index')  
    else:
        return Response({})
        #return redirect('Products:index')



#Decrease Item from cart
@api_view(['GET','POST'])
def decrease_item(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_table = Order.objects.filter(user=request.user, ordered=False)

    if order_table.exists():
        order = order_table[0]
        if order.orderItems.filter(item=item).exists():
            cart_check = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if cart_check.quantity>1:
                 cart_check.quantity-=1
                 cart_check.save()
                 return Response({})
                 #return redirect('Order:cartView')
            else:
                order.orderItems.remove(cart_check)
                cart_check.delete()
                return Response({})
                #return redirect('Products:index')

        else:
            return Response({})
            #return redirect('Products:index')  
    else:
        return Response({})
        #return redirect('Products:index')