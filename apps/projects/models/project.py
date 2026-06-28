import uuid

from django.conf import settings
from django.db import models

from apps.teams.models import Team

class Project(models.Model):
    class Visibility(models.TextChoices):
        PRIVATE = "private","Private"
        PUBLIC = "public","Public"
        
    class Status(models.TextChoices):
        ACTIVE = "active","Active"
        ARCHIVED= "archived","ARCHIVED"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="projects")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_projects")
    
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="project_logos/",blank=True, null=True)
    visibility = models.CharField(max_length=20, choices=Visibility.choices, default=Visibility.PRIVATE)
    
    status= models.CharField(max_length=20, choices = Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("team","slug")
        
    def __str__(self):
        return self.name