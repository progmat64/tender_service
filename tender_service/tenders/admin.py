from django.contrib import admin

from .models import Employee, Organization, Bid, Review, Tender

admin.site.register(Organization)
admin.site.register(Employee)
admin.site.register(Tender)
admin.site.register(Bid)
admin.site.register(Review)
