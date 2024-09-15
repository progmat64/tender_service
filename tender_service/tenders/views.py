from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tender, Bid
from .serializers import TenderSerializer, BidSerializer

class PingView(APIView):
    def get(self, request):
        return Response('ok', status=status.HTTP_200_OK)

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
            return Response({"error": "Cannot rollback to a future version"}, status=status.HTTP_400_BAD_REQUEST)

        # Для простоты представим, что сохраняем предыдущие версии в поле `history`, но можно использовать более сложные механизмы
        tender.version = version
        tender.save()

        serializer = TenderSerializer(tender)
        return Response(serializer.data, status=status.HTTP_200_OK)
