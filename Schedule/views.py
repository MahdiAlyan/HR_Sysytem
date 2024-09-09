from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance,LeaveRequest

# Create your views here.


def Schedule(request):
    attendance_records = Attendance.objects.filter(user=request.user)
    leave_requests = LeaveRequest.objects.filter(user=request.user)
    return render(request, 'Schedule/sched.html',{
        'attendance_records': attendance_records,
        'leave_requests': leave_requests,

    })


def request_day_off(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')
        LeaveRequest.objects.create(user=request.user, start_date=start_date, end_date=end_date, reason=reason)
        return redirect('schedule')

    return render(request, 'schedule/request_day_off.html')
