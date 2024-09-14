from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import CustomUserChangeForm, CustomUserCreationForm
from core.models import CustomUser

# Create your views here.


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'HR/hr.html', {'Users': users})


def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('users')
        else:
            messages.error(request, 'Error creating user. Please check the form.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'HR/create_user.html', {'form': form})


def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to user list after saving
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'HR/edit_user.html', {'form': form, 'user': user})


def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('user_list')
