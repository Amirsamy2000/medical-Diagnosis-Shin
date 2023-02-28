from django.shortcuts import render

def listdoctors(request):
    return render(request,'doctor/doctor.html')
