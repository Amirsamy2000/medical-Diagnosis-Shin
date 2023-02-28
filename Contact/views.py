from django.shortcuts import render

def contactFun(requset):
    return render (requset,'contact/contact.html')
