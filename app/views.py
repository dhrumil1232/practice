from multiprocessing import context
from xml.dom.minicompat import EmptyNodeList
from django.http import HttpResponse
from django.shortcuts import render
from .models import department, employee, role

def IndexPageView(request):
    return render(request,"app/index.html")
def OurworkPageView(request):
    return render(request,"app/ourworks.html")
def AboutusPageView(request):
    return render(request,"app/aboutus.html")
def ContactusPageView(request):
    return render(request,"app/contactus.html")
def EmployeeData(request):
    all_data = employee.objects.all()
    
    return render(request,"app/employee.html",{'key1':all_data})
def DeleteData(request):
    d = employee.objects.get(id=1)
    d.delete()
    return render(request,"app/delete.html")
def CreateData(request):    
    a = employee(id=1,employee_name="Dhrumil",employee_description="Dhrumil",department_id=1,role_id=1)
    a.save()
    return render(request,"app/create.html")   
def UpdateData(request):
    b = employee.objects.get(id=3)
    b.employee_name ="Harshil"
    b.employee_description = "Harshil"
    b.save()
    return render(request,"app/update.html")