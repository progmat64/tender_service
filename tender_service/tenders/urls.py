from django.urls import path
from .views import PingView, TenderListView
from .views import TenderCreateView, TenderListView, TenderEditView, TenderRollbackView, BidCreateView

urlpatterns = [
    path('ping/', PingView.as_view()),
    path('tenders/', TenderListView.as_view()),
    path('tenders/new/', TenderCreateView.as_view()),
    path('tenders/<uuid:tender_id>/edit/', TenderEditView.as_view()),
    path('tenders/<uuid:tender_id>/rollback/<int:version>/', TenderRollbackView.as_view()),
    path('bids/new/', BidCreateView.as_view()),
]