from django import forms
from .models import CustomUser  # Assuming your profile is part of the Employee model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image']  # Only include the profile_image field


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'gender', 'profile_image', 'start_date', 'job_title', 'department')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'gender', 'profile_image', 'start_date', 'job_title', 'department')

