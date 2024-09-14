from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Attendance,LeaveRequest

# Create your views here.


def Schedule(request):
    attendance_records = Attendance.objects.filter(CustomUser=request.user)
    leave_requests = LeaveRequest.objects.filter(CustomUser=request.user)
    return render(request, 'Schedule/sched.html', {
        'attendance_records': attendance_records,
        'leave_requests': leave_requests,
    })


def request_day_off(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')
        LeaveRequest.objects.create(CustomUser_id=request.user_id, start_date=start_date,
                                    end_date=end_date, reason=reason)
        return redirect('schedule')

    return render(request, 'schedule/request_day_off.html')


def check_in(request):
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(CustomUser=request.user, date=today)

    if not attendance.checked_in:
        attendance.checked_in = True
        attendance.in_at = timezone.now().time()
        attendance.save()

    return redirect('schedule')


def check_out(request):
    today = timezone.now().date()
    attendance = get_object_or_404(Attendance, CustomUser=request.user, date=today)

    if attendance.checked_in and not attendance.checked_out:
        attendance.checked_out = True
        attendance.out_at = timezone.now().time()
        attendance.save()

    return redirect('schedule')

