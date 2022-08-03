'''
Points logics 
    - Profile 
'''

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

## importing models
from accounts.models.profile import (
    Profile
)

### Request view for Adding points when API will be HIT

class PointAddView(APIView):

    def post(self,request):
        ## Fetching the data from Client server
        profile_ID = request.data.get('profile_ID')
        points = request.data.get('points')

        get_profile = Profile.objects.filter(id=profile_ID).first()

        ## checking the obj if exists 
        if get_profile :
            get_profile.points_gained += int(points)
            get_profile.save()

            return Response({
                'success':'Points Added'
            },status=status.HTTP_202_ACCEPTED)
            
        else:
            return Response({
                'Error':'Profile ID didn`t match'
            },status=status.HTTP_404_NOT_FOUND)


### Request view for Loosing points when API will be HIT

class PointLooseView(APIView):

    def post(self,request):

        ## Fetching the data from Client server
        profile_ID = request.data.get('profile_ID')
        points = request.data.get('points')

        get_profile = Profile.objects.filter(id=profile_ID).first()

        ## checking the obj if exists 
        if get_profile :

            ## if points is 0 the return False
            if get_profile.points_gained <= 0 :
                return Response({
                    'Error':'User Has 0.0 Point'
                },status=status.HTTP_406_NOT_ACCEPTABLE)

            ## else points will be minus
            else:
                get_profile.points_gained -= int(points)
                get_profile.save()

                return Response({
                    'success':'Points Loose'
                },status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'Error':'Profile ID didn`t match'
            },status=status.HTTP_404_NOT_FOUND)
    


            