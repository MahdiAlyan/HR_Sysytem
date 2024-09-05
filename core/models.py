from django.db import models
from django.utils import timezone
# Create your models here.


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True, unique=True)
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    job_title = models.CharField(max_length=150)
    hour_rate = models.FloatField(default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
