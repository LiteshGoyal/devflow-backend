from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ("email",)
    
    list_display = ("email","username",'is_staff','is_verified',)
    
    search_fields = ("email","username")
    readonly_fields=("last_login","created_at","updated_at",)
    
    fieldsets = (
        (None,{"fields":("email","password")}),
        ("Personal",{
            "fields":(
                "username",
                "first_name",
                "last_name",
                "avatar",
                "bio",
            )
        }),
        ("OAuth",{
            "fields":(
                "github_id","google_id",
            )
        }),
        ("Dates",{
            "fields":("last_login",)
        }),
    )
    
    add_fieldsets=((None, {
        "classes":("wide",),
        "fields":("email","username","password1","password2")
    }))