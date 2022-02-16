from django.urls import path,include
from . import views
urlpatterns = [
path("",views.IndexPageView,name="indexpage"),
path("ourworks/",views.OurworkPageView,name="ourworkpage"),
path("aboutus/",views.AboutusPageView,name="contactus"),
path("contactus/",views.ContactusPageView,name="aboutuspage"),
path("employee/",views.EmployeeData,name="employeepage"),
path("delete/",views.DeleteData,name="deletedata"),
path("create/",views.CreateData,name="createdata"),
path("update/",views.UpdateData,name="updatedata"),


]