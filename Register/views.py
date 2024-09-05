from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/Home/')  # Redirect to home if login is successful
        else:
            messages.error(request, 'Invalid username or password')  # Show error if authentication fails
            return redirect('signin')

    return render(request, 'Register/Signin.html')


# Sign Out View
def signout(request):
    logout(request)
    return render(request, 'Register/Signout.html')
