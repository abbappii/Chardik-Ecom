from django.shortcuts import render
from django.http import HttpResponse
from MainApplication import settings
store_id = settings.store_id
api_key = settings.Api_key

from sslcommerz_lib import SSLCOMMERZ 


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status

from orders.database.cart_order import Order
from MainApplication.scripts.pay import unique_tran_id_generate
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


class payment(APIView):
    def get(self, request, format = None):
        settings = { 'store_id': store_id, 'store_pass': api_key, 'issandbox': True }
        sslcommez = SSLCOMMERZ(settings)

        customer = request.user.profile
        order = Order.objects.filter(customer=customer, payment_complete=False).last()

        addr1 = str(order.address_shipping.city)
        addr2 = str(order.address_shipping.area) 

        addr = str(addr1 + ', ' + addr2)

        total_amount = order.total
        print(total_amount)

        tran_id = unique_tran_id_generate

        reverse_url1 = request.build_absolute_uri(reverse('success_payment'))

        reverse_url2 = request.build_absolute_uri(reverse('pay_failed'))
        reverse_url3 = request.build_absolute_uri(reverse('pay_failed'))

        post_body = {}

        post_body['value_a'] = order.id
        post_body['value_b'] = customer.id

        post_body['total_amount'] = total_amount
        post_body['currency'] = "BDT"
        post_body['tran_id'] = tran_id
        
        post_body['success_url'] = reverse_url1

        post_body['fail_url'] = reverse_url2
        post_body['cancel_url'] = reverse_url3
        post_body['emi_option'] = 0
        post_body['cus_name'] = customer.full_name
        post_body['cus_email'] = 'example@gmail.com'
        post_body['cus_phone'] = order.mobile
        post_body['cus_add1'] = addr
        post_body['cus_city'] = addr1
        post_body['cus_country'] = ""
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1

        post_body['product_name'] = "Cosmetics for women"
        post_body['product_category'] = "Body care"
        post_body['product_profile'] = "physical"

        response = sslcommez.createSession(post_body)
        # print(response)
        return Response(response, status=status.HTTP_200_OK)
        


@api_view(['POST'])
@csrf_exempt 
def payment_success(request):

    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST

        print(payment_data['value_a'])
       
        # order id 
        order_id = payment_data['value_a']
        order = Order.objects.get(id=order_id)
        print(order)
        order.payment_complete = True 
        order.save()    

        # return Response(payment_data, status=status.HTTP_200_OK) 
        return render(request, 'index.html')



@api_view(['POST'])
@csrf_exempt 
def refund_request(request):

    settings = { 'store_id': store_id, 'store_pass': api_key, 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)

    if request.method == 'POST' or request.method == 'post':
        data = request.POST
        print(data)
        bank_tran_id = data['bank_tran_id']

        refund_amount =  data['refund_amount']
        refund_remarks = data['refund_remarks']

        response = sslcommez.init_refund(bank_tran_id,refund_amount,refund_remarks)
        # print(response)
        return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt 
def refund_status(request):

    settings = { 'store_id': store_id, 'store_pass': api_key, 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)

    if request.method == 'POST' or request.method == 'post':
        data = request.POST

        refund_ref_id = data['refund_ref_id']
        response = sslcommez.query_refund_status(refund_ref_id)
        # print(response)
        return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])    
@csrf_exempt
def failed(request):
    return render(request, 'failed.html')