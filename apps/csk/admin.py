from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import (
    UserCall, 
    MasterUser,
)


class MasterUserAdmin(UserAdmin):
    """Регистрация модели CustomUser в админ панели"""

    model = MasterUser

    fieldsets = (
        ('Information', {
            'fields': (
                'full_name',
                'password',
                'service_master',
                'is_busy'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),
    )

    list_display = (
        'full_name',
        'password',
        'service_master',
        'is_superuser',
        'is_staff',
        'is_active'
    )

    list_filter = ('full_name',)

    search_fields = ('full_name',)

    filter_horizontal = ()

    ordering = ('full_name',)

    add_fieldsets = (
        ("User Details", {'fields': ('username', 'phone_number', 'full_name', 'service_master', 'password1', 'password2', 'is_busy', 'is_superuser', 'is_staff', 'is_active',)}),
    )


# admin.site.register(MasterUserAdmin)



admin.site.register(UserCall)
admin.site.register(MasterUser, MasterUserAdmin)