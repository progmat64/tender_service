from django.contrib import admin

from .models import Bid, Employee, Organization, Review, Tender

admin.site.register(Organization)
admin.site.register(Employee)
admin.site.register(Tender)
admin.site.register(Bid)
admin.site.register(Review)
