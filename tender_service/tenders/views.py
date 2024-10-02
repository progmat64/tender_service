from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Bid, Employee, Organization, Review, Tender
from .serializers import BidSerializer, ReviewSerializer, TenderSerializer


def home_view(request):
    text = """
    Сервис проведения тендеров

    API:
    GET /api/ping/
    GET /api/tenders/
    POST /api/tenders/new
    GET /api/tenders/my?username=user1
    PATCH /api/tenders/1/edit
    PUT /api/tenders/1/rollback/2
    POST /api/bids/new
    GET /api/bids/my?username=user1
    PUT /api/bids/1/rollback/2
    GET /api/bids/1/reviews?authorUsername=user2&organizationId=1
    """
    return HttpResponse(text, content_type="text/plain; charset=utf-8")


class PingView(APIView):
    def get(self, request):
        return Response("ok", status=status.HTTP_200_OK)


class TenderListView(APIView):
    def get(self, request):
        tenders = Tender.objects.all()
        serializer = TenderSerializer(tenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TenderCreateView(APIView):
    def post(self, request):
        serializer = TenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BidCreateView(APIView):
    def post(self, request):
        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TenderListView(APIView):
    def get(self, request):
        tenders = Tender.objects.all()
        serializer = TenderSerializer(tenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TenderStatusView(APIView):
    def get(self, request, tender_id):
        try:
            tender = Tender.objects.get(id=tender_id)
            serializer = TenderSerializer(tender)
            return Response(serializer.data.get("status"), status=status.HTTP_200_OK)
        except Tender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, tender_id):
        try:
            tender = Tender.objects.get(id=tender_id)
        except Tender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        new_status = request.query_params.get("status", None)
        username = request.query_params.get("username", None)

        if not new_status or not username:
            return Response({"error": "Status and username are required"}, status=status.HTTP_400_BAD_REQUEST)

        valid_statuses = [choice[0] for choice in Tender.STATUS_CHOICES]
        if new_status not in valid_statuses:
            return Response({"error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}"},
                            status=status.HTTP_400_BAD_REQUEST)

        tender.status = new_status
        tender.save()

        serializer = TenderSerializer(tender)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TenderEditView(APIView):
    def patch(self, request, tender_id):
        try:
            tender = Tender.objects.get(id=tender_id)
        except Tender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TenderSerializer(tender, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TenderRollbackView(APIView):
    def put(self, request, tender_id, version):
        try:
            tender = Tender.objects.get(id=tender_id)
        except Tender.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if version >= tender.version:
            return Response(
                {"error": "Cannot rollback to a future version"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tender.version = version
        tender.save()

        serializer = TenderSerializer(tender)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyTenderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.query_params.get("username", None)
        if username is None:
            return Response(
                {"error": "Username is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        tenders = Tender.objects.filter(creator__username=username)

        if not tenders.exists():
            return Response(
                {"error": "No tenders found for this user"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TenderSerializer(tenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyBidListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.query_params.get("username", None)
        if username is None:
            return Response(
                {"error": "Username is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        bids = Bid.objects.filter(creator__username=username)

        if not bids.exists():
            return Response(
                {"error": "No bids found for this user"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TenderBidListView(APIView):
    def get(self, request, tender_id):
        try:
            bids = Bid.objects.filter(tender_id=tender_id)
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BidSerializer(bids, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BidEditView(APIView):
    def patch(self, request, bid_id):
        try:
            bid = Bid.objects.get(id=bid_id)
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BidSerializer(bid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BidRollbackView(APIView):
    def put(self, request, bid_id, version):
        try:
            bid = Bid.objects.get(id=bid_id)
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if version >= bid.version:
            return Response(
                {"error": "Cannot rollback to a future version"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        bid.version = version
        bid.save()

        serializer = BidSerializer(bid)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TenderBidReviewsView(APIView):
    def get(self, request, tender_id):
        author_username = request.query_params.get("authorUsername", None)
        organization_id = request.query_params.get("organizationId", None)

        if not author_username or not organization_id:
            return Response(
                {"error": "Author username and organization ID are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            organization = Organization.objects.get(id=organization_id)
            author = Employee.objects.get(username=author_username)
            bids = Bid.objects.filter(
                tender_id=tender_id, creator=author, organization=organization
            )

            if not bids.exists():
                return Response(
                    {
                        "error": "No bids found for this author in the specified tender and organization"
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            reviews = Review.objects.filter(bid__in=bids)
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Organization.DoesNotExist:
            return Response(
                {"error": "Organization not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Employee.DoesNotExist:
            return Response(
                {"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND
            )
