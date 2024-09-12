from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # You should create this form to handle user creation
    form = CustomUserChangeForm  # You should create this form to handle user changes

    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'job_title', 'department', 'is_staff',  'bio', 'phone_number')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gender', 'department')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'user__username', 'user__email', 'bio', 'phone_number')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'gender', 'profile_image', 'bio')}),
        ('Employment', {'fields': ('start_date', 'job_title', 'department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'gender', 'profile_image', 'start_date', 'job_title', 'department'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
