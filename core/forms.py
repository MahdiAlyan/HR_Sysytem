from django import forms
from .models import CustomUser  # Assuming your profile is part of the Employee model


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image']  # Only include the profile_image field



