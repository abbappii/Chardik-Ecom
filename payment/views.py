
from urllib import response
from MainApplication import settings
store_id = settings.store_id
api_key = settings.Api_key

from django.http import HttpResponse

from sslcommerz_lib import SSLCOMMERZ 


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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
        order = Order.objects.get(customer=customer)
        total_amont = order.total
        print(total_amont)
        tran_id = unique_tran_id_generate

        # for item in order.items:
        #     p_name = item.item.product_name

        reverse_url1 = request.build_absolute_uri(reverse('success_payment'))

        reverse_url2 = request.build_absolute_uri(reverse('order_url'))
        reverse_url3 = request.build_absolute_uri(reverse('order_url'))

        post_body = {}
        post_body['total_amount'] = total_amont
        post_body['currency'] = "BDT"
        post_body['tran_id'] = tran_id
        
        post_body['success_url'] = reverse_url1

        post_body['fail_url'] = reverse_url2
        post_body['cancel_url'] = reverse_url3
        post_body['emi_option'] = 0
        post_body['cus_name'] = customer.full_name
        post_body['cus_email'] = order.email
        post_body['cus_phone'] = customer.phone
        post_body['cus_add1'] = customer.address
        post_body['cus_city'] = customer.city
        post_body['cus_country'] = customer.country
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1

        post_body['product_name'] = "Cosmetics for women"
        post_body['product_category'] = "Body care"
        post_body['product_profile'] = "physical"

        response = sslcommez.createSession(post_body)
        return Response(response)


@api_view(['POST'])
@csrf_exempt 
def payment_success(request):

    settings = { 'store_id': store_id, 'store_pass': api_key, 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)

    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST

        post_body = {}
        post_body['tran_id'] =  payment_data['tran_id']
        post_body['val_id'] =  payment_data['val_id']
        post_body['amount'] = payment_data['amount']
        post_body['card_type'] = payment_data['card_type']
        post_body['store_amount'] = payment_data['store_amount']
        post_body['card_no'] = payment_data['card_no']
        post_body['bank_tran_id'] = payment_data['bank_tran_id']
        post_body['status'] = payment_data['status']
        post_body['tran_date'] = payment_data['tran_date']

        post_body['error'] = payment_data['error']

        post_body['currency'] = payment_data['currency']
        post_body['card_issuer'] = payment_data['card_issuer']
        post_body['card_brand'] = payment_data['card_brand']

        post_body['card_sub_brand'] = payment_data['card_sub_brand']

        post_body['card_issuer_country'] = payment_data['card_issuer_country']
        post_body['card_issuer_country_code'] = payment_data['card_issuer_country_code']
        post_body['store_id'] = payment_data['store_id']
        post_body['verify_sign'] = payment_data['verify_sign']
        post_body['verify_key'] = payment_data['verify_key']
        post_body['verify_sign_sha2'] = payment_data['verify_sign_sha2']
        post_body['currency_type'] = payment_data['currency_type']
        post_body['currency_amount'] = payment_data['currency_amount']
        post_body['currency_rate'] = payment_data['currency_rate']
        post_body['base_fair'] = payment_data['base_fair']
        post_body['value_a'] = payment_data['value_a']
        post_body['value_b'] = payment_data['value_b']
        post_body['value_c'] = payment_data['value_c']
        post_body['value_d'] = payment_data['value_d']
        post_body['risk_level'] = payment_data['risk_level']
        post_body['risk_title'] = payment_data['risk_title']

        response = sslcommez.hash_validate_ipn(post_body)
        print(response)
        return Response(response) 


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
        print(response)
        return Response(response)


@api_view(['POST'])
@csrf_exempt 
def refund_status(request):

    settings = { 'store_id': store_id, 'store_pass': api_key, 'issandbox': True }
    sslcommez = SSLCOMMERZ(settings)

    if request.method == 'POST' or request.method == 'post':
        data = request.POST

        refund_ref_id = data['refund_ref_id']
        response = sslcommez.query_refund_status(refund_ref_id)
        print(response)
        return Response(response)