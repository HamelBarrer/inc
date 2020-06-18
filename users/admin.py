from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    Client,
    Employee,
    Provider,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('role',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )


admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Provider)
