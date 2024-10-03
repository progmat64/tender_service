from rest_framework import serializers

from .models import (
    Bid,
    Employee,
    Organization,
    OrganizationResponsible,
    Review,
    Tender,
)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationResponsible
        fields = "__all__"


class TenderSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        slug_field="username", queryset=Employee.objects.all()
    )

    class Meta:
        model = Tender
        fields = "__all__"


class BidSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
        slug_field="username", queryset=Employee.objects.all()
    )

    class Meta:
        model = Bid
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", queryset=Employee.objects.all()
    )

    class Meta:
        model = Review
        fields = "__all__"
