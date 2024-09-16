# Generated by Django 5.1.1 on 2024-09-16 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=50, unique=True)),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("IE", "IE"), ("LLC", "LLC"), ("JSC", "JSC")],
                        default="LLC",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Bid",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CREATED", "Created"),
                            ("PUBLISHED", "Published"),
                            ("CANCELED", "Canceled"),
                        ],
                        default="CREATED",
                        max_length=10,
                    ),
                ),
                ("version", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.employee",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrganizationResponsible",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.organization",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.employee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review_text", models.TextField()),
                ("rating", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.employee",
                    ),
                ),
                (
                    "bid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.bid",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tender",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("service_type", models.CharField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CREATED", "Created"),
                            ("PUBLISHED", "Published"),
                            ("CLOSED", "Closed"),
                        ],
                        default="CREATED",
                        max_length=10,
                    ),
                ),
                ("version", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.employee",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tenders.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bid",
            name="tender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tenders.tender",
            ),
        ),
    ]
