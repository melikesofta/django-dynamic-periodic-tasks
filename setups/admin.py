from django.contrib import admin

from .models import Setup


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = [
        '__str__'
    ]
