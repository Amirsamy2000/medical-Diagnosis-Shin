import re
from django.shortcuts import render
from.forms import mainForm
def indexFun(requset):
    form=mainForm()
    description=''
    link=''
    if requset.method=='POST':
        form=mainForm(requset.POST)
        if form.is_valid():
            cd=form.cleaned_data
            description=cd['description']
            link=cd['link']


    return render(requset,'home/main.html',{'form':form ,'description':description,'link':link})