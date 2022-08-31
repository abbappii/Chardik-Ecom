from ast import Return
from products.database.products import Products
from django.shortcuts import get_object_or_404
from orders.database.cart_order import Cart 
from orders.database.coupon import Order
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view



#add to cart function
@api_view(['GET','POST'])
def add_to_cart(request, pk):
    '''
    the item exist in product database or not
    if the item is exist in Product database than it 
    will create . if its not exist it will be 404
    '''
    item = get_object_or_404(Products, pk=pk)
    '''
    The item already exsist in the cart or it will not exist it will create one
    '''
    cart_check = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    '''
    For current user there is any active order or not. If the 
    ordered==True than we dont have any headache lol
    '''
    order_item = Order.objects.filter(user=request.user, ordered=False)
    '''
    if the item already exist in cart and order is exsit than the 
    quantity will be increase 1
    '''
    if order_item.exists():
        order = order_item[0]
        if order.orderItems.filter(item=item).exists():
            cart_check[0].quantity +=1
            cart_check[0].save()
            return Response({})

            '''
            Else it will add the item in active or exsit order table
        '''  
        else:
            order.orderItems.add(cart_check[0])
            order.save()
            return Response({})
            
        '''
        if the cart is empty and there is no active or exsist order than
        create a cart and order and add new item 
    '''
    else:
        order = Order(user=request.user)
        order.save()
        order.orderItems.add(cart_check[0])
        return Response({})



# show item in cart
@api_view(['GET','POST'])     
def cart_view(request):
    cart = Cart.objects.filter(user=request.user, purchased=False)
    order = Order.objects.filter(user=request.user, ordered=False)

    if cart.exists() and order.exists():
        cart_order = order[0]
        return Response({})
        #return render(request, 'Order/shopping-cart.html', context={'cart':cart, 'order':cart_order})

    else:
        return Response({})
        #return redirect('Products:index')

