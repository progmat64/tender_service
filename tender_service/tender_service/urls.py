from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('tenders.urls')),  # Включаем маршруты из приложения tenders
]
