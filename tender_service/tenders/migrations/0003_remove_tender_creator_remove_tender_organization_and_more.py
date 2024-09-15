# Generated by Django 5.1.1 on 2024-09-15 15:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tenders", "0002_employee_tender_service_type_alter_bid_creator_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tender",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="tender",
            name="organization",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="password",
        ),
        migrations.AddField(
            model_name="organization",
            name="type",
            field=models.CharField(
                choices=[("IE", "IE"), ("LLC", "LLC"), ("JSC", "JSC")],
                default="LLC",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.CreateModel(
            name="OrganizationResponsible",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
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
        migrations.DeleteModel(
            name="Bid",
        ),
        migrations.DeleteModel(
            name="Tender",
        ),
    ]
