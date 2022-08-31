'''
THis file contains the logics of 
    - user permission 
    - validate user when they login 
        based on their permission 
'''


from rest_framework.permissions import BasePermission
from accounts.models.profile import Profile
from django.http import JsonResponse


# def classPermission()

# Is Admin Permission 

class IsAdmin(BasePermission):
    message = 'User Is Not an Admin'
    def has_permission(self, request, view):

        try:
            # print(request.user.profile.get_permission_id)
            return bool(request.user.is_authenticated and request.user.profile \
                 and 1 in request.user.profile.get_permission_id)
            
        except Profile.DoesNotExist:
            return JsonResponse({'Error':'Sorry User is not an Admin'})



# Is Manager Permission 

class IsManager(BasePermission):
    message = 'User Is Not a Manager'
    def has_permission(self, request, view):

        try:
            return bool(request.user.is_authenticated and request.user.profile \
                and 2 in request.user.profile.get_permission)
        except Profile.DoesNotExist:
            return JsonResponse({'Error':'Sorry User is not a Manager'})



# Is Stuff Permission 

class IsStuff(BasePermission):
    message = 'User Is Not a Stuff'
    def has_permission(self, request, view):

        try:
            return bool(request.user.is_authenticated and request.user.profile \
                and 3 in request.user.profile.get_permission)
        except Profile.DoesNotExist:
            return JsonResponse({'Error':'Sorry User is not a Stuff'})



# Is Customer
class IsCustomer(BasePermission):
    message = 'User Is Not a Customer'
    def has_permission(self, request, view):

        try:
            return bool(request.user.is_authenticated and request.user.profile \
                and 4 in request.user.profile.get_permission_id)
        except Profile.DoesNotExist:
            return JsonResponse({'Error':'Sorry User is not a Customer'})
