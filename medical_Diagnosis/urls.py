"""medical_Diagnosis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth_login.views import LoginFun
from auth_login.views import homeFun
from auth_login.views import Reg_patientFun
from auth_login.views import Reg_doctorFun
from home.views import indexFun
from services.views import showServices
from doctor.views import listdoctors
from Contact.views import contactFun
from profilePatient.views import profileFun
from about.views import aboutFun
from SingUp.views import SingUpUserFun


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginFun,name='log'),
    path('home', homeFun,name='home'),
    path('register',Reg_patientFun),
    path('register2',Reg_doctorFun),
    path('index',indexFun),
    path('service',showServices,name='service'),
    path('doctor',listdoctors,name='doctor'),
    path('contact',contactFun,name='contact'),
    path('profile',profileFun,name='profile'),
    path('about',aboutFun,name='about'),
    path('SingUPUserPage',SingUpUserFun,name='regisertuser'),

 

   
]
