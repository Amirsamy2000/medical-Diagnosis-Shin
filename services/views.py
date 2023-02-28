from django.shortcuts import render
def showServices(request):
    return render(request,"services/service.html")
