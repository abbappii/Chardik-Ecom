
# import string
# import random

# from orders.database.cart_order import Order
# import datetime
# date = datetime.date.today()
# s_date = str(date)

# # order id get 

# # example = ch20220809(order_id)

# date_str= ''.join(e for e in s_date if e.isalnum())
# code = 'ch' + date_str

# def random_code(size=10, chars = code + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# def unique_refID_generate(instance):
#     r_code = random_code()
#     take = instance.__class__
#     take_exits = take.objects.filter(ref_code=code).exists()
#     if take_exits:
#         return r_code
#     return code


