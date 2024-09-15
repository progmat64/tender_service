from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Менеджер для пользовательской модели Employee (если используете свою модель)
class EmployeeManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field is required')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)


# Кастомная модель пользователя Employee (если нужно использовать свою модель пользователя)
class Employee(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


# Модель Organization
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Модель Tender
class Tender(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Created'),
        ('PUBLISHED', 'Published'),
        ('CLOSED', 'Closed')
    ]
    
    SERVICE_TYPE_CHOICES = [
        ('Construction', 'Construction'),
        ('IT', 'IT'),
        ('Consulting', 'Consulting')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES, default='Construction')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CREATED')
    version = models.IntegerField(default=1)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Используем Employee, если это ваша кастомная модель
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Модель Bid
class Bid(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Created'),
        ('PUBLISHED', 'Published'),
        ('CANCELED', 'Canceled'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CREATED')
    version = models.IntegerField(default=1)
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Используем Employee, если это ваша кастомная модель
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Увеличиваем версию только при обновлении объекта (если уже существует)
        if self.pk is not None:
            self.version += 1
        super(Bid, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
