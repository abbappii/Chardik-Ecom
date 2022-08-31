'''
This file contains the logics of
    - after registering the user 
        customer ID will be created automaticatlly
'''

import string
import random

def random_code(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_batchID_generate(instance):
    code = random_code()

    take = instance.__class__
    take_exits = take.objects.filter(batch_no=code).exists()
    if take_exits:
        return unique_batchID_generate(instance)
    return code
