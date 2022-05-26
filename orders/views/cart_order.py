
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from orders.database.cart_order import *

from orders.serializers import CartSerializer, CartProductSerializer, OrderSerializer
from products.database.products import Products


class MyCart(viewsets.ViewSet):
    permission_classes=[IsAuthenticated, ]
    authentication_classes=[TokenAuthentication, ]
    
    def list(self,request):
        query = Cart.objects.filter(customer=request.user)
        serializers = CartSerializer(query,many=True)
        all_data=[]
        for cart in serializers.data:
            cart_product = CartProduct.objects.filter(cart=cart["id"])
            cart_product_serializer = CartProductSerializer(cart_product,many=True)
            cart["cartproduct"] = cart_product_serializer.data
            all_data.append(cart)
        return Response(all_data)

class AddtoCartView(GenericAPIView):
    # permission_classes=[IsAuthenticated, ]
    # authentication_classes=[TokenAuthentication, ]
    
    def post(self,request):
        # get product 
        product_id = int(request.data.get('id'))
        print(product_id)
        product_obj = Products.objects.get(id=product_id)
        # print(product_obj,"product_obj")  
   
        # filter for cart exist or not and cart order complete status    
        cart_cart = Cart.objects.filter(customer=request.user).filter(complete=False).first()
        
        try:
            # if any cart exits 
            if cart_cart:
                this_product_in_cart = cart_cart.cartproduct_set.filter(product=product_obj)

                # check product already in cart or not 
                if this_product_in_cart.exists():
                    cartprod_uct = CartProduct.objects.filter(product=product_obj).filter(cart__complete=False).first()
                    cartprod_uct.quantity += 1
                    cartprod_uct.subtotal += product_obj.new_price
                    cartprod_uct.save()
                    cart_cart.total += product_obj.new_price
                    cart_cart.save()

                # if product is not in cart add this product to cart 
                else:
                    cart_product_new=CartProduct.objects.create(
                        cart = cart_cart,
                        price  =product_obj.new_price,
                        quantity = 1,
                        subtotal = product_obj.new_price
                    )
                    cart_product_new.product.add(product_obj)
                    cart_cart.total +=product_obj.new_price
                    cart_cart.save()

            # if this user has no existing cart, create a new cart and add this product to newly created cart
            else:
                Cart.objects.create(customer=request.user.profile,total=0,complete=False)
                new_cart = Cart.objects.filter(customer=request.user.profile).filter(complete=False).first()
                cart_product_new=CartProduct.objects.create(
                        cart = new_cart,
                        price  =product_obj.new_price,
                        quantity = 1,
                        subtotal = product_obj.new_price
                    )
                cart_product_new.product.add(product_obj)
                # print("NEW CART PRODUCT CREATED")    
                new_cart.total +=product_obj.new_price
                new_cart.save()

            response_mesage = {'error':False,'message':"Product add to card successfully","productid":product_id}
        
        except:
            response_mesage = {'error':True,'message':"Product Not add!Somthing is Wromg"}

        return Response(response_mesage)


class OrderViewset(viewsets.ViewSet):
    authentication_classes=[TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def list(self,request):
        query = Order.objects.filter(cart__customer = request.user)
        serializers = OrderSerializer(query,many=True)
        all_data = []
        for order in serializers.data:
            cartproduct = CartProduct.objects.filter(cart_id=order['cart']['id'])
            cartproduct_serializer = CartProductSerializer(cartproduct,many=True)
            order['cartproduct'] = cartproduct_serializer.data
            all_data.append(order)
        return Response(all_data)
        
    def retrieve(self,request,pk=None):
        try:
            queryset = Order.objects.get(id=pk)
            serializers = OrderSerializer(queryset)
            data = serializers.data
            all_date=[]
            cartproduct = CartProduct.objects.filter(cart_id=data['cart']['id'])
            cartproduct_serializer = CartProductSerializer(cartproduct,many=True)
            data['cartproduct'] = cartproduct_serializer.data
            all_date.append(data)
            response_message = {"error":False,"data":all_date}
        except:
            response_message = {"error":True,"data":"No data Found for This id"}

        return Response(response_message)

    def destroy(self,request,pk=None):
        try:
            order_obj=Order.objects.get(id=pk)
            cart_obj = Cart.objects.get(id=order_obj.cart.id)
            order_obj.delete()
            cart_obj.delete()
            responsemessage = {"erroe":False,"message":"Order delated","order id":pk}
        except:
            responsemessage = {"erroe":True,"message":"Order Not Found"}
        return Response(responsemessage)

    def create(self,request):
        cart_id = request.data["cartId"]
        cart_obj = Cart.objects.get(id=cart_id)
        address = request.data["address"]
        mobile = request.data["mobile"]
        email = request.data["email"]
        cart_obj.complit=True
        cart_obj.save()
        created_order = Order.objects.create(
            cart=cart_obj,
            address=address,
            mobile=mobile,
            email=email,
            total=cart_obj.total,
            discount=3,
            #Order status = Order recieved 
        )
        return Response({"message":"order Resebed","cart id":cart_id,"order id":created_order.id})


class Updatecart(APIView):

    def post(self,request):
        cart_product_id = request.data['id']
        cart_product = CartProduct.objects.get(id=cart_product_id)
        
        cart_obj = CartProduct.cart

        cart_product.quantity += 1
        cart_obj.subtotal +=cart_product.price
        cart_product.save()

        cart_obj.total += cart_product.price
        cart_obj.save() 

        return Response({'message': "CartProduct is added"})

class Editcart(APIView):

    def post(self,request):
        cart_product_id = request.data['id']
        # cart product define
        cart_product = CartProduct.objects.get(id=cart_product_id)
        cart_obj = CartProduct.cart

        cart_product.quantity -= 1
        cart_obj.subtotal -=cart_product.price
        cart_product.save()

        cart_obj.total -= cart_product.price
        cart_obj.save() 
        
        if cart_product.quantity == 0:
            cart_product.delete()

        return Response({'message': "CartProduct is added"})

class DeleteCart(APIView):
    def post(self,request):
        cart_product = CartProduct.objects.get(id = request.data['id'])
        cart_product.delete()



# test code

from rest_framework.generics import GenericAPIView

class AddtoCartViews(GenericAPIView):
    # permission_classes=[IsAuthenticated, ]
    # authentication_classes=[TokenAuthentication, ]
    
    def post(self,request):
        # get product 
        product_id = request.data.get('id')
        print(product_id)
        # print(int(request.data['ID']))
    
        return Response({'data':'data'})