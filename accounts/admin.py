from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("email", "first_name", "last_name", "is_staff")
    fieldsets = ((None, {"fields": ("email", "password")}), ("Informazioni personali", {"fields": ("first_name", "last_name")}), ("Permessi", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}), ("Date", {"fields": ("last_login", "date_joined")}))
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)
    search_fields = ("email", "first_name", "last_name")
