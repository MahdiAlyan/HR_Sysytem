from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], null=True, blank=True)
    profile_image = models.ImageField(upload_to="./Media/uploaded_images",
                                      blank=True, null=True, default='images/default.png')
    start_date = models.DateField(default=timezone.now)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    hour_rate = models.FloatField(default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.username


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name
