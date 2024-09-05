from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User


# Sign In View

def Home(request):
    if request.user.is_authenticated:
        return render(request, 'core/Home.html',{

        })
    return redirect("/Register/signin/")


def profile(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=user_id)
        return render(request, 'core/profile.html', {
            'user': user
        })
