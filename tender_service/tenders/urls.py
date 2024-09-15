from django.urls import path
from .views import PingView, TenderListView, TenderCreateView, TenderEditView, TenderRollbackView, BidCreateView

urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('tenders/', TenderListView.as_view(), name='tender-list'),
    path('tenders/new/', TenderCreateView.as_view(), name='tender-create'),
    path('tenders/<int:tender_id>/edit/', TenderEditView.as_view(), name='tender-edit'),
    path('tenders/<int:tender_id>/rollback/<int:version>/', TenderRollbackView.as_view(), name='tender-rollback'),
    path('bids/new/', BidCreateView.as_view(), name='bid-create'),
]
