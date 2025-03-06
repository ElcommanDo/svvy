from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import *
from django.conf import settings
from django.utils.html import format_html
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="70" />', obj.image.url)
        else:
            return format_html('<img src="/static/img/default.jpg" height="50" />')

    image_preview.short_description = 'Image Preview'

    def profile_link(self, obj):
        """Generate a clickable link to the user profile details page."""
        base_url = settings.BASE_URL  # Define BASE_URL in settings
        profile_url = f"{base_url}/user-data/{obj.id}/"
        return format_html('<a href="{}" target="_blank">View Profile</a>', profile_url)

    profile_link.short_description = "Profile Link"  # Custom column name

    list_display = (
        "image_preview",
        "name",
        "phone",
        "profile_link",
        "address",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )

    list_filter = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": (
            "name",
            "image",
                    "phone",
                    "address",
                    "email", 
                    "facebook_page",            
                    "groups"
                    )}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    
                    "user_permissions",
                )
            },
        ),
        ("Dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "phone",
                    "password1",
                    "password2",
                    "address",
                    "email",

                ),
            },
        ),
    )
    search_fields = ("phone","name")
    ordering = ("phone",)

