from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def SingUpUserFun(requset):
    form=UserCreationForm(requset.POST or None , requset.FILES or None)
    if form.is_valid(): 
        form.save()
    return render(requset,'SingUp/SingUPUser.html',{'form':form})
