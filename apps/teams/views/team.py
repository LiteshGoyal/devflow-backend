from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.teams.models import Team
from apps.teams.serializers import TeamSerializer

class TeamListCreateAPIView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        teams = Team.objects.filter(organization__owner=request.user)
        serializer = TeamSerializer(teams, many=True)
        
        return Response({
            "success":True,
            "data":serializer.data
        })
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({
                "success":True,
                "data":serializer.data,
            },status=status.HTTP_201_CREATED)
            
        return Response({
            "success":False,
            "errors":serializer.errors,
        },status=status.HTTP_400_BAD_REQUEST)