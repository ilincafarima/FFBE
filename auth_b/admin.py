from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('role', 'membership_status', 'worker_type', 'rating')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'role', 'membership_status', 'worker_type', 'profile_picture', 'rating')}
        ),
    )
    list_display = ('username', 'email', 'role', 'membership_status', 'rating', 'is_staff')
    list_filter = ('role', 'membership_status', 'is_staff', 'rating')
    search_fields = ('username', 'email', 'role', 'membership_status', 'worker_type')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
