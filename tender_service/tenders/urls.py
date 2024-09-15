from django.urls import path
from .views import (
    PingView, TenderListView, TenderCreateView, TenderEditView, TenderRollbackView, 
    BidCreateView, MyTenderListView, MyBidListView, TenderBidListView, BidEditView, BidRollbackView, TenderBidReviewsView
)

urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('tenders/', TenderListView.as_view(), name='tender-list'),
    path('tenders/new/', TenderCreateView.as_view(), name='tender-create'),
    path('tenders/<int:tender_id>/edit/', TenderEditView.as_view(), name='tender-edit'),
    path('tenders/<int:tender_id>/rollback/<int:version>/', TenderRollbackView.as_view(), name='tender-rollback'),
    path('tenders/my/', MyTenderListView.as_view(), name='tender-my'),
    path('bids/new/', BidCreateView.as_view(), name='bid-create'),
    path('bids/my/', MyBidListView.as_view(), name='bid-my'),
    path('bids/<int:tender_id>/list/', TenderBidListView.as_view(), name='bid-list'),
    path('bids/<int:bid_id>/edit/', BidEditView.as_view(), name='bid-edit'),
    path('bids/<int:bid_id>/rollback/<int:version>/', BidRollbackView.as_view(), name='bid-rollback'),
    path('bids/<int:tender_id>/reviews/', TenderBidReviewsView.as_view(), name='bid-reviews'),
]
