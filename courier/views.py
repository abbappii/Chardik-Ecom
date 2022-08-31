
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from courier.serializers import pathao_endpoint_serializers
import requests

# Create your views here.



# Get Access Token 
@api_view(['POST'])
def pathao_view(request):

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json"
    }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/issue-token"
    data={
        "client_id": "262",
        "client_secret": "19vSoYnXyGnJkYuhJ8Htj5XA93ZkylyLGYmiZWG9",
        "username": "info.chardike@gmail.com",
        "password": "lovePathao",
        "grant_type": "password"
    }
    
    response = requests.post(pathao_api, json=data , headers=headers)
    print("Response", response)
    return Response(data=response.json())





# # Get  Refresh Token
@api_view(['POST'])
def pathao_refresh_token(request):
    pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
    pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()
   


    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json"
    }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/issue-token"
    data={
        "client_id": "262",
        "client_secret": "19vSoYnXyGnJkYuhJ8Htj5XA93ZkylyLGYmiZWG9",
       
        "refresh_token": pathao_api_accesstoken_response_json['refresh_token'],  # dont know how to implement Refresh token
        "grant_type": "refresh_token"
    }
    
    response = requests.post(pathao_api, json=data , headers=headers)
    return Response(data=response.json())








# # Get  cities
@api_view(['GET'])
def pathao_get_cites(request):

    pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
    pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()
    

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(pathao_api_accesstoken_response_json['access_token']),
    }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/countries/1/city-list"
    response = requests.get(pathao_api, headers=headers)
    return Response(data=response.json())



# # Get  zone
@api_view(['GET'])
def pathao_get_zone(request):

    pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
    pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()
   

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(pathao_api_accesstoken_response_json['access_token']),
    }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/cities/1/zone-list"
    response = requests.get(pathao_api, headers=headers)
    return Response(data=response.json())




# Get  area
@api_view(['GET'])
def pathao_get_area(request):

    pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
    pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(pathao_api_accesstoken_response_json['access_token']),
    }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/zones/1/area-list"
    response = requests.get(pathao_api, headers=headers)
    return Response(data=response.json())






# Create Store
@api_view(['POST'])
def pathao_create_store(request):

    store_name=request.data.get('name')
    contact_name=request.data.get('contact_name')
    contact_number=request.data.get('contact_number')
    address=request.data.get('address')
    secondary_contact=request.data.get('secondary_contact')
    city_id=request.data.get('city_id')
    zone_id=request.data.get('zone_id')
    area_id=request.data.get('area_id')



    pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
    pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()
    

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(pathao_api_accesstoken_response_json['access_token']),
    }

    data={
            "name": store_name,
            "contact_name": contact_name,
            "contact_number": contact_number,
            "address":address,
            "secondary_contact": secondary_contact,
            "city_id": city_id,
            "zone_id": zone_id,
            "area_id": area_id
            }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/stores"
    response = requests.post(pathao_api, json=data, headers=headers) 
    return Response(data=response.json())


    # # Get  Store
@api_view(['GET'])
def pathao_get_store(request):
    pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
   
    pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()
   

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(pathao_api_accesstoken_response_json['access_token']),
       
    }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/stores"
    response = requests.get(pathao_api, headers=headers)
    return Response(data=response.json())
   




# Create order
@api_view(['POST'])
def pathao_create_order(request):


    store_id=  request.data.get('store_id')
    merchant_order_id=  request.data.get('merchant_order_id')
    recipient_name= request.data.get('recipient_name')
    recipient_phone=  request.data.get('recipient_phone')
    recipient_address= request.data.get('recipient_address')
    recipient_city=  request.data.get('recipient_city')
    recipient_zone=  request.data.get('recipient_zone')
    recipient_area=  request.data.get('recipient_area')
    delivery_type=  request.data.get('delivery_type')
    item_type=  request.data.get('item_type')
    special_instruction= request.data.get('special_instruction')
    item_quantity=  request.data.get('item_quantity')
    item_weight= request.data.get('item_weight') 
    amount_to_collect=  request.data.get('amount_to_collect')
    item_description=  request.data.get('item_description')



    pathao_accesstoken_api='https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    pathao_api_accesstoken_response=requests.post(pathao_accesstoken_api)
    pathao_api_accesstoken_response_json=pathao_api_accesstoken_response.json()
    

    headers={
        "Accept": "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {}".format(pathao_api_accesstoken_response_json['access_token']),
    }

    data={
            "store_id": store_id,
            "merchant_order_id": merchant_order_id,
            "recipient_name":recipient_name,
            "recipient_phone": recipient_phone,
            "recipient_address":recipient_address,
            "recipient_city": recipient_city,
            "recipient_zone": recipient_zone,
            "recipient_area": recipient_area,
            "delivery_type": delivery_type,
            "item_type": item_type,
            "special_instruction":special_instruction,
            "item_quantity": item_quantity,
            "item_weight": item_weight,
            "amount_to_collect": amount_to_collect,
            "item_description": item_description
            }

    pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/orders"
    response = requests.post(pathao_api, json=data, headers=headers) 
    return Response(data=response.json())


from django.conf import settings
from rest_framework import status

# Price Calculation
@api_view(['POST'])
def pathao_price_calculation(request):
    #first logic 
    
    # store_id=request.data.get('store_id')
    # item_type=request.data.get('item_type')
    # delivery_type=request.data.get('delivery_type')
    # item_weight=request.data.get('item_weight')
    # recipient_city=request.data.get('recipient_city')
    # recipient_zone=request.data.get('recipient_zone')


    # pathao_accesstoken_api='http://127.0.0.1:8000/courier/pathao/'
    # pathao_accesstoken_api_response=requests.post(pathao_accesstoken_api)
    # pathao_accesstoken_api_response_json=pathao_accesstoken_api_response.json()
    # print(pathao_accesstoken_api_response_json)

    # headers={
    #     "Accept": "application/json",
    #     "Content-Type" : "application/json",
    #     "Authorization" : "Bearer{}".format(pathao_accesstoken_api_response_json['access_token'])
    # }

    # data={
    #         "store_id": store_id,
    #         "item_type": item_type,
    #         "delivery_type": delivery_type,
    #         "item_weight": item_weight,
    #         "recipient_city": recipient_city,
    #         "recipient_zone": recipient_zone
    #         }
    # print("Json data",data)

    # pathao_api = "https://hermes-api.p-stageenv.xyz/aladdin/api/v1/merchant/price-plan"
    # response = requests.post(pathao_api, json=data, headers=headers)
    # print("Response", response)
    # return Response(data=response.json())



    #second logic
    payload_data = {
            # "client_id": settings.PATHAO_CLIENT_ID,
            # "client_secret": settings.PATHAO_CLIENT_SECRET,
            # "username": settings.PATHAO_CLIENT_EMAIL,
            # "password": settings.PATHAO_PASSWORD,
            # "grant_type": settings.PATHAO_GRANT_TYPE,

            "client_id": "262",
            "client_secret": "19vSoYnXyGnJkYuhJ8Htj5XA93ZkylyLGYmiZWG9",
            "username": "info.chardike@gmail.com",
            "password": "lovePathao",
            "grant_type": "password"
        }
    print('payload data = ', payload_data)
    #pathao_base_url = settings.PATHAO_BASE_URL
    pathao_base_url = 'https://oyster-app-7ulvb.ondigitalocean.app/courier/pathao/'
    print('base url = ', pathao_base_url)
    # issue_token_url = pathao_base_url + "/aladdin/api/v1/issue-token"
    # print('issue_token_url = ', issue_token_url)

    authentication = requests.request('POST', pathao_base_url, data=payload_data)
    print('authentication = ', authentication)
    authentication_json = authentication.json()
    print('authentication_json = ', authentication_json)
    print('authentication_json access_token = ', authentication_json['access_token'])
    access_token = authentication_json['access_token']
        #
    headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token,
        }
    print('price plan api headers = ', headers)
    pathao_price_plan_api = 'https://hermes-api.p-stageenv.xyz/aladdin/api/v1/merchant/price-plan'

    data = {
            "store_id": "111",
            "item_type": "2",
            "delivery_type": "48",
            "item_weight": "0.5",
            "recipient_city": 1,
            "recipient_zone": 50
        }
    print('payload = ', data)
    price_plan = requests.post(pathao_price_plan_api, json=data, headers=headers)
    print('price_plan = ', price_plan)
    pathao_price_plan = price_plan.json()
    print('pathao_price_plan = ', pathao_price_plan)
    pathao_price_plan_data = pathao_price_plan
    print("message data = ", pathao_price_plan_data)

    dict_response = {
            'error': False,
            'message': 'price plan',
            'data': pathao_price_plan_data
        }
    return Response(dict_response, status=status.HTTP_200_OK)

    

    
        

