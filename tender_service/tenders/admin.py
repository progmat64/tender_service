from django.contrib import admin
from .models import Employee, Organization, Tender, Bid

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'created_at', 'updated_at']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'status', 'organization', 'creator', 'created_at']

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'version', 'tender', 'organization', 'creator', 'created_at']
