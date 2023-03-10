# Generated by Django 4.1.5 on 2023-01-23 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                ("date", models.DateTimeField()),
                ("due_date", models.DateTimeField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("PAID", "Paid"),
                            ("UNPAID", "Unpaid"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        default="UNPAID",
                        max_length=15,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemLine",
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
                ("quantity", models.IntegerField()),
                ("description", models.TextField(max_length=500)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("taxed", models.BooleanField()),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billing.invoice",
                    ),
                ),
            ],
        ),
    ]
