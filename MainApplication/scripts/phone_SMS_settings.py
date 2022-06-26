'''
THis file contains the custom thread 
Phone Verification 
 '''

from email import message
import threading
import requests
import random

# importing models
from accounts.models.profile import Profile

'''
Phone OTP verification Settings
    Username 
    password 
    add 
'''

phone_OTP_Username = "01784502888"
phone_OTP_Password = "CHARDIKE@0066"


### SMS OPT functions for sending OTP
# verification 
# reset Password

class SMS_of_Phone_Verification(threading.Thread):
    def __init__(self,number,profile_ID):
        self.number = number
        self.profile_ID = profile_ID
        threading.Thread.__init__(self)

    def run(self):
        try:
            otp = random.randint(111111, 999999)
            url = f"http://66.45.237.70/api.php?username={phone_OTP_Username}&\
                password={phone_OTP_Password}&number=88{self.number}&\
                message=Your Charidike.com OTP is {otp}"

            payload  = {}
            
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request("POST", url, headers=headers, data = payload)

            # get the current Profile id and save the OTP
            profile = Profile.objects.get(id=self.profile_ID)
            profile.phone_otp = otp
            profile.save()

            return response
        except Exception as e:
            print(e)


### SMS functions for sending Messages
# Order 
# Others Update


class SMS_for_Phone_Message(threading.Thread):
    def __init__(self,number,phone_message):
        self.number = number
        self.message = phone_message
        threading.Thread.__init__(self)

    def run(self):
        try:

            url = f"http://66.45.237.70/api.php?username={phone_OTP_Username}&\
                password={phone_OTP_Password}&number=88{self.number}&\
                message={self.message}"

            payload  = {}
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request("POST", url, headers=headers, data = payload)

            return response
        except Exception as e:
            print(e)
