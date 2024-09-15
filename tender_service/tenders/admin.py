from django.contrib import admin

from .models import Employee, Organization

admin.site.register(Organization)
admin.site.register(Employee)
