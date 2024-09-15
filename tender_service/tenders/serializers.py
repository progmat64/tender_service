from rest_framework import serializers
from .models import Tender, Bid
from .models import Organization
from django.contrib.auth.models import User  # используем модель User

class TenderSerializer(serializers.ModelSerializer):
    # Поля для связи с другими моделями
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Tender
        fields = ['id', 'name', 'description', 'service_type', 'status', 'version', 'organization', 'creator', 'created_at', 'updated_at']


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'name', 'description', 'status', 'version', 'tender', 'organization', 'creator', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context['request']
        validated_data['creator'] = request.user  # Устанавливаем пользователя как создателя предложения
        return super().create(validated_data)
