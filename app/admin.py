from django.contrib import admin
from .models import employee,role,department

admin.site.register(role)
admin.site.register(department)
admin.site.register(employee)


