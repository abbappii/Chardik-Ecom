
from MainApplication import settings
store_id = settings.store_id
api_key = settings.Api_key


from sslcommerz_lib import SSLCOMMERZ 


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from orders.database.cart_order import Order
from MainApplication.scripts.pay import unique_tran_id_generate
from django.urls import reverse

class payment(APIView):
    def get(self, request, format = None):
        settings = { 'store_id': store_id, 'store_pass': api_key, 'issandbox': True }
        sslcommez = SSLCOMMERZ(settings)
        
        customer = request.user.profile
        order = Order.objects.get(customer=customer)
        total_amont = order.total
        tran_id = unique_tran_id_generate

        reverse_url1 = request.build_absolute_uri(reverse('order_url'))
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

        post_body['product_name'] = ""
        post_body['product_category'] = ""
        post_body['product_profile'] = ""

        response = sslcommez.createSession(post_body)
        return Response(response)