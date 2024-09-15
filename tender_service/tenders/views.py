from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework import status
from django.contrib.auth.models import User
from .models import Tender, Bid, Organization
from .serializers import TenderSerializer, BidSerializer

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer

    # Создание нового тендера
    def create(self, request, *args, **kwargs):
        organization = Organization.objects.get(id=request.data.get('organization'))
        creator = User.objects.get(id=request.data.get('creator'))  # Используем ID пользователя
        tender_data = request.data.copy()
        tender_data['organization'] = organization.id
        tender_data['creator'] = creator.id

        serializer = self.get_serializer(data=tender_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Фильтрация тендеров по типу услуг (например, Construction, IT)
    def list(self, request):
        service_type = request.query_params.get('serviceType', None)
        if service_type:
            tenders = Tender.objects.filter(service_type=service_type)
        else:
            tenders = Tender.objects.all()
        serializer = TenderSerializer(tenders, many=True)
        return Response(serializer.data)

    # Возвращаем тендеры, созданные текущим пользователем
    @action(detail=False, methods=['get'])
    def my(self, request):
        username = request.query_params.get('username')
        user = User.objects.get(username=username)
        tenders = Tender.objects.filter(creator=user)
        serializer = TenderSerializer(tenders, many=True)
        return Response(serializer.data)

    # Редактирование тендера
    @action(detail=True, methods=['patch'])
    def edit(self, request, pk=None):
        tender = self.get_object()
        serializer = TenderSerializer(tender, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # Откат тендера к предыдущей версии
    @action(detail=True, methods=['put'])
    def rollback(self, request, pk=None, version=None):
        tender = Tender.objects.get(pk=pk)
        if tender.version >= int(version):
            tender.version = int(version)
            tender.save()
            serializer = TenderSerializer(tender)
            return Response(serializer.data)
        return Response({'error': 'Invalid version'}, status=400)


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    # Редактирование предложения
    @action(detail=True, methods=['patch'])
    def edit(self, request, pk=None):
        bid = self.get_object()
        serializer = BidSerializer(bid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # Откат версии предложения
    @action(detail=True, methods=['put'])
    def rollback(self, request, pk=None, version=None):
        bid = Bid.objects.get(pk=pk)
        if bid.version >= int(version):
            bid.version = int(version)
            bid.save()
            serializer = BidSerializer(bid)
            return Response(serializer.data)
        return Response({'error': 'Invalid version'}, status=400)

# Эндпоинт для проверки доступности сервера
@api_view(['GET'])
def ping(request):
    return Response("ok", status=200)
