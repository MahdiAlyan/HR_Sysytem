from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm
from .models import CustomUser
from django.contrib import messages


# Sign In View


def Home(request):
    if request.user.is_authenticated:
        return render(request, 'core/Home.html', {

        })
    return redirect("/signin/")


def profile(request, user_id):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(id=user_id)
        return render(request, 'core/profile.html', {
            'user': user
        })


def edit_profile_pic(request):
    return upload_profile_pic(request)


@login_required
def remove_profile_pic(request):
    user_profile = request.user
    if user_profile.profile_image is not 'images/default.png':
        user_profile.profile_image = 'Media/images/default.png'
        user_profile.save()
        messages.success(request, 'Profile picture removed successfully.')
    return redirect('profile', user_id=request.user.id)


@login_required
def upload_profile_pic(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = request.user  # Get the current user
            user_profile.profile_image = form.cleaned_data['profile_image']
            user_profile.save()  # Save the updated user profile
            messages.success(request, 'Profile picture uploaded successfully.')
            return redirect('profile', user_id=request.user.id)
        else:
            messages.error(request, 'Failed to upload your profile picture. Please try again.')
    else:
        form = ProfilePictureForm()

    return render(request, 'core/upload_profile_picture.html', {'form': form})
