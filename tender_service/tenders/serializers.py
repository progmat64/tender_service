from rest_framework import serializers
from .models import Employee, Organization, OrganizationResponsible
from .models import Tender, Bid

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class OrganizationResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationResponsible
        fields = '__all__'


class TenderSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(slug_field='username', queryset=Employee.objects.all())
    
    class Meta:
        model = Tender
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'


