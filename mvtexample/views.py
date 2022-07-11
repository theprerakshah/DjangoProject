from django.http import HttpResponse
from django.shortcuts import render
from mvtexample.form import NameForm

def index(request):
    return HttpResponse("hello how are you there")

def index2(request):
   return HttpResponse("my name is prerak")

def eform(request):
    return render(request, 'newform.html')

def myform(request):
    
    empname="not logged in"
    empid="not logged in"
    empdept="not logged in"
    empphone="not logged in"
    

    if request.method=="POST":
        myform1=NameForm(request.POST)
        if myform1.is_valid():
            empname=myform1.cleaned_data['empname']
            empid=myform1.cleaned_data['empid']
            empdept=myform1.cleaned_data['empdept']
            empphone=myform1.cleaned_data['empphone']
    else:
        myform1=NameForm()

    return render(request, 'helloemp.html',{"empname" : empname,"empid" : empid,"empdept" : empdept,"empphone" : empphone})  
    
   
