from django.contrib import admin
from apps.teams.models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=("name","organization","created_at",)
    search_fields=("name",)
    
