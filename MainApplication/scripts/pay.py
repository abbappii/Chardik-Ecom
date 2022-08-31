

import string
import random

def random_code(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_tran_id_generate(instance):
    code = random_code()

    take = instance.__class__
    take_exits = take.objects.filter(customer_ID=code).exists()
    if take_exits:
        return unique_tran_id_generate(instance)
    return code
