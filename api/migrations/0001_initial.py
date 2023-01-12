# Generated by Django 4.1.4 on 2023-01-10 15:18

import cloudinary.models
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
            name="Category",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(default="Learning", max_length=150, unique=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ToDo",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=150, unique=True)),
                ("description", models.TextField()),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        blank=True,
                        default=None,
                        max_length=255,
                        null=True,
                        verbose_name="image",
                    ),
                ),
                ("dueDate", models.DateField()),
                ("assigned", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPEN", "Open"),
                            ("CLOSED", "Closed"),
                            ("IN-PROGRESS", "InProgress"),
                            ("BLOCKED", "Blocked"),
                            ("COMPLETED", "Completed"),
                        ],
                        default="OPEN",
                        max_length=150,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("LOW", "Low"),
                            ("MEDIUM", "Medium"),
                            ("HIGH", "High"),
                            ("OPTIONAL", "Optional"),
                        ],
                        default="LOW",
                        max_length=150,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.category"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
                "abstract": False,
            },
        ),
    ]
