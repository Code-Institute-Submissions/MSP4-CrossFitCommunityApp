from django.contrib import admin
from .models import CustomGroup
from django.contrib.auth.models import User


class CustomGroupAdmin(admin.ModelAdmin):
    fields = ('name', 'group_users', 'admin')
    list_display = (
        'name',
        'admin'
    )

admin.site.register(CustomGroup, CustomGroupAdmin)