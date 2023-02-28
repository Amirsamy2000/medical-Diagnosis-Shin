
from django.db import models
from auth_login.models import Register_patient

class treatment_readable(models.Model):
    disease=models.CharField(null=False,max_length=50)
    id_disease=models.IntegerField()
    treat1=models.CharField(null=False,max_length=50)
    treat2=models.CharField(null=False,max_length=50)
    treat3=models.CharField(null=False,max_length=50)
    treat4=models.CharField(null=False,max_length=50)
    def __str__(self) :
        return self.disease

class diseas_t_pathient(models.Model):
    patient=models.ForeignKey(Register_patient,on_delete=models.CASCADE)
    id_disease=models.IntegerField()




