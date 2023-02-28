from django.contrib import admin
from .models import Register_doctor,Register_patient

# Register your models here.ad
admin.site.register((Register_patient,Register_doctor))
