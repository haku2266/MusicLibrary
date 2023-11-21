from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel


# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info',
            {
                'fields': (
                    'profile_img',
                )
            }
        )
    )


admin.site.register(CustomUserModel, CustomUserAdmin)
