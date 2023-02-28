from django.contrib import admin
from .models import treatment_readable,diseas_t_pathient

# Register your models here.ad
admin.site.register((diseas_t_pathient,treatment_readable))
