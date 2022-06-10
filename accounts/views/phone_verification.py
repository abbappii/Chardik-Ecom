
import requests

username = '01784502888'
password = 'CHARDIKE@0066'


def SMSsend(number):

    url = f"http://66.45.237.70/api.php?username={username}&password={password}&number={number}&message=Charidike.com OTP is 76879"

    payload  = {}
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    print("done")

    print(response.text.encode('utf8'))