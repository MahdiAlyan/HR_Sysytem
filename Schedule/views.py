from django.shortcuts import render

# Create your views here.


def Schedule(request):
    return render(request, 'Schedule/sched.html')