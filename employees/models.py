from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # New field added
    hire_date = models.DateField()
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
