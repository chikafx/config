from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'email', 'password']
    list_editable=['last_name']
