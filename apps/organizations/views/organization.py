from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.organizations.models import Organization
from apps.organizations.serializers import OrganizationSerializer

class OrganizationListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        organizations= Organization.objects.filter(owner=request.user)
        serializer = OrganizationSerializer(organizations, many=True)
        
        return Response({"success":True, "data":serializer.data})
    
    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({
                "success":True,
                "message":"Organization created successfully",
                "data":serializer.data,
            },status=status.HTTP_201_CREATED)
            
        return Response({
            "success":False,
            "errors":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

class OrganizationDetailAPIView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get_object(self, pk, user):
        return Organization.objects.get(pk=pk, owner=user)
        
    def get(self, request,pk):
        organization = self.get_object(pk, request.user)
        print(organization.name)
        print(organization.slug)
        print(organization.description)
        serializer = OrganizationSerializer(organization)
        
        return Response({
            "success":True,
            "data":serializer.data,
        })
        
    def put(self, request, pk):
        organization = self.get_object(pk, request.user)
        serializer = OrganizationSerializer(organization, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success":True,
                "message":"Organization updated successfully",
                "data":serializer.data,
            })
            
        return Response({
            "success":False,
            "errors": serializer.errors,
        },status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        organization = self.get_object(pk, request.user)
        organization.delete()
        
        return Response({
            "success":True,
            "message":"Organization deleted successfully",
        })