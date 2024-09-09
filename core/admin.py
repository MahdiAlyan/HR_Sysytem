from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import CustomUser
from . import models
# Register your models here.


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(models.Department)
admin.site.register(User, CustomUser)