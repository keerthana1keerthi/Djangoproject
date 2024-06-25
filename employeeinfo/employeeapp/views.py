from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Employee
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def add(request,a,b):
    c=a+b
    return HttpResponse('The addition of 2 numbers is'+str(c))

def Employee_list(request):
    Employees=Employee.objects.all()

    return render(request,'Employee_list.html',{'Employees':Employees})


