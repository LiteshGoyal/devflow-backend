from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.serializers import RegisterSerializer

class RegisterAPIView(APIView):
    permission_classes=[]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            
            return Response({
                "success":True,
                "message":"Registration Successful",
                "data":{
                    "user":{
                        
                            "id":str(user.id),
                            "email":user.email,
                            "username":user.username,
                        },
                        "tokens":{
                            "refresh":str(refresh),
                            "access":str(refresh.access_token),
                        },
                    },
            },)
        return Response({
            "success":False,"errors":serializer.errors,
        },status=status.HTTP_400_BAD_REQUEST)