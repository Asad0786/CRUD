from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=20,choices=[('IT Infrastructure','IT'),
                                     ('Software Development', 'SDE'),
                                     ('Consultancy','HR'),
                                     ('Banking','Banking')])
    contact = models.IntegerField()
    active = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=256)

    def __str__(self) -> str:
        return self.name + " - "+self.location

class Employee(models.Model):
    name = models.CharField(max_length=30)
    emp_type = models.CharField(max_length=10, choices=[('PT','Permanent'),
                                                        ('PR','Probhiton'),
                                                        ('C','Contractiual'),
                                                        ('T', 'Temp')])
    active = models.BooleanField(default=True)
    salary = models.IntegerField(max_length=100000)
    emp_id = models.IntegerField(max_length=999999999999)
    company = models.ForeignKey(Company, on_delete=models.CASCADE )

    def __str__(self) -> str:
        return self.name +"-"+ str(self.emp_id)


