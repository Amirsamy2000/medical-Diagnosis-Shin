from pydoc import describe
from tkinter import CASCADE
from django.db import models
from auth_login.models import Register_doctor

# Create your models here.
class home_Advert(models.Model):
    prodect=models.CharField(max_length=40,null=False)
    describes=models.TextField(max_length=300,null=False)
    link=models.CharField(max_length=300)
    id_Advert=models.ForeignKey(Register_doctor,on_delete=models.CASCADE)
    def __str__(self) :
        return self.prodect