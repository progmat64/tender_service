from django.contrib import admin
from django.urls import include, path

from tenders.views import home_view

urlpatterns = [
    path("api/", include("tenders.urls")),
    path("admin/", admin.site.urls),
    path("", home_view),
]
