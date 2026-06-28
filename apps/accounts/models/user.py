import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# from common.models import BaseModel
from apps.accounts.managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True,)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="avatars/",blank=True, null=True,)
    bio = models.TextField(blank=True,)
    
    is_verified = models.BooleanField(default=False,)
    
    github_id = models.CharField(max_length=255, blank=True, null=True)
    google_id = models.CharField(max_length=255,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=["username"]
    objects = UserManager()
    
    class Meta:
        db_table = "users"
        
    def __str__(self):
        return self.email