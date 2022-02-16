from django.db import models

# Create your models here.
class role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.CharField(max_length=50)
    class Meta:
        db_table = "role"
    


class department(models.Model):
    department_name =models.CharField(max_length=50)
    department_description = models.CharField(max_length=55)
    class Meta:
        db_table = "department"
class employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_description = models.CharField(max_length=60)
    role = models.OneToOneField(role,on_delete=models.CASCADE)
    department = models.OneToOneField(department,on_delete=models.CASCADE)
    class Meta:
        db_table = "employee"        

