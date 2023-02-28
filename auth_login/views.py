
from operator import is_not
from django.shortcuts import render
from.forms import LoginForm
from.forms import patientForm
from.forms import doctorForm

def LoginFun(requset):
    form=LoginForm()
    m=''
    m1=''
    if(requset.method=='POST'):
        form=LoginForm(requset.POST)
        if form.is_valid():
            cd=form.cleaned_data
            f=cd['password']
            
            m1=f
            print(m1)
            if f:
                m='good work'
            else:
                m='not good work'    
           
            

    return render(requset,'Login/login.html',{'form':form,'m':m})                

def homeFun(requset):
    return render(requset,'home.html')

def Reg_patientFun(requset):
    form=patientForm()
    return render(requset,'Regiseter/regiseter_patient.html',{'form':form})
def Reg_doctorFun(requset):
    form=doctorForm()
    return render(requset,'Regiseter/regiseter_doctor.html',{'form':form})

