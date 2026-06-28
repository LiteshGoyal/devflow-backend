from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.projects.models import Project
from apps.projects.serializers import ProjectSerializer

class ProjectListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.filter(created_by=request.user)
        serializer = ProjectSerializer(projects, many=True)

        return Response({
            "success":True,
            "data":serializer.data,
        })
        
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user,)
            return Response({
                "success":True,
                "data":serializer.data
            },
                status=status.HTTP_201_CREATED,)
            
        return Response({
            "success":False,
            "errors":serializer.errors,
        },status=status.HTTP_400_BAD_REQUEST,)