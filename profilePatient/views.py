from django.shortcuts import render
from.forms import profileForm
def profileFun(request):
    form=profileForm()
    return render(request,'profile/profile.html',{'form':form})

