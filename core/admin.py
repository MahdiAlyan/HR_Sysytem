from django.contrib import admin
from . import models
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_id', 'department', 'date_joined')
    list_filter = ('department',)
    search_fields = ('first_name', 'last_name', 'employee_id')


admin.site.register(models.Department)
admin.site.register(models.Employee)
