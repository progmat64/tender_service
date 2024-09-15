from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Organization(models.Model):
    ORGANIZATION_TYPES = [
        ("IE", "IE"),
        ("LLC", "LLC"),
        ("JSC", "JSC"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=ORGANIZATION_TYPES, default="LLC")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrganizationResponsible(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Tender(models.Model):
    STATUS_CHOICES = [
        ("CREATED", "Created"),
        ("PUBLISHED", "Published"),
        ("CLOSED", "Closed"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    service_type = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="CREATED")
    version = models.IntegerField(default=1)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bid(models.Model):
    STATUS_CHOICES = [
        ("CREATED", "Created"),
        ("PUBLISHED", "Published"),
        ("CANCELED", "Canceled"),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="CREATED")
    version = models.IntegerField(default=1)
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Review(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    author = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Автор отзыва
    review_text = models.TextField()
    rating = models.IntegerField(default=1)  # Рейтинг, например от 1 до 5
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.author.username} on {self.bid.name}'