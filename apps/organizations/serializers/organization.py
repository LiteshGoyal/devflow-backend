from rest_framework import serializers
from apps.organizations.models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    
    class Meta:
        model=Organization
        fields=("id","name","slug","description","logo","owner","created_at","updated_at")
        read_only_fields = (
            "id",
            "owner",
            "created_at",
            "updated_at",
        )