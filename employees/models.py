from django.db import models
from departments.models import Department  
from datetime import datetime
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # New field added
    hire_date = models.DateField(default=datetime.now())
    job_title = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
