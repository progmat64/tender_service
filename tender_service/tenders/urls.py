from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenderViewSet, BidViewSet, ping

router = DefaultRouter()
router.register(r'tenders', TenderViewSet)
router.register(r'bids', BidViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ping/', ping),  # Эндпоинт для проверки доступности
    path('tenders/my', TenderViewSet.as_view({'get': 'my'})),  # получение тендеров пользователя
]
