from django.db import models
from django.conf import settings
from django.utils import timezone
from core.models import CustomUser
from datetime import datetime

# Create your models here.


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('on_leave', 'On Leave'),
        ('late', 'Late'),
    ]

    CustomUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)  # Date of attendance
    checked_in = models.BooleanField(default=False)  # Whether the employee checked in
    in_at = models.TimeField(null=True, blank=True)  # Actual check-in time
    checked_out = models.BooleanField(default=False)  # Whether the employee checked out
    out_at = models.TimeField(null=True, blank=True)  # Actual check-out time
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='absent')

    def __str__(self):
        return f"{CustomUser.username} - {self.date} - {self.status}"

    @property
    def worked_hours(self):
        if self.checked_in and self.checked_out:
            delta = datetime.combine(self.date, self.out_at) - datetime.combine(self.date, self.in_at)
            return delta.total_seconds() / 3600  # Returns hours worked
        return 0


class LeaveRequest(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('sick', 'Sick Leave'),
        ('vacation', 'Vacation'),
        ('personal', 'Personal Leave'),
    ]
    CustomUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES, default='sick')
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{CustomUser.username} - {self.leave_type} - {self.start_date} to {self.end_date}"
