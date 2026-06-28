from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class MeAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({
            "success":True,
            "data":{
                "id":str(user.id),
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "avatar": user.avatar.url if user.avatar else None,
                "bio": user.bio,
                "is_verified": user.is_verified,
            },
        },status= status.HTTP_200_OK)
        