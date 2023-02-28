
from django.db import models

# Create your models here.
class Register_doctor(models.Model):
    username=models.CharField(max_length=100,null=False)
    email=models.EmailField(null=False)
    password=models.CharField(max_length=100,null=False)
    phone=models.IntegerField(null=False)
    brith_data=models.DateTimeField(null=True)
    specialtion=models.CharField(max_length=100,null=False)
    address=models.CharField(max_length=100)

    def __str__(self) :
        return self.username


class Register_patient(models.Model):
    username=models.CharField(max_length=100,null=False)
    email=models.EmailField(null=False)
    password=models.CharField(max_length=100,null=False)
    phone=models.IntegerField(null=False)
    brith_data=models.DateTimeField(null=True)
    address=models.CharField(max_length=100)
    def __str__(self) :
        return self.username



        
        


