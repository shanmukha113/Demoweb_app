from django.shortcuts import render
from django.http import HttpResponse
from BasicwebApp.models import Form
# Create your views here.

def home(request):
  if request.method=='GET':
    return render(request,"home.html")
  else:
    name=request.POST.get("name")
    email=request.POST.get("email")
    age=request.POST.get("age")
    dob=request.POST.get("dateofbirth")
    Form(name=name,mail=email,age=age,date_of_birth=dob).save()
    return render(request,"home.html",{'valid':'data saved'})

def dataretrive(request):
    form=Form.objects.all()
    return render(request,"retrive.html",{'forms':form})
