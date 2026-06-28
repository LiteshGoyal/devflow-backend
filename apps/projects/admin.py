from django.contrib import admin
from apps.projects.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name","team","visibility","status")
    
    search_fields = ("name","slug")
    
    list_filter = ("visibility", "status")
    