# Generated by Django 4.2.18 on 2025-03-03 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0001_initial"),
        ("signup", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coordinator",
            fields=[
                (
                    "coordinator_name",
                    models.CharField(max_length=25, primary_key=True, serialize=False),
                ),
                (
                    "coordinator_type",
                    models.CharField(
                        choices=[
                            ("club", "Club Coordinator"),
                            ("department", "Department Coordinator"),
                        ],
                        max_length=10,
                    ),
                ),
                ("email", models.CharField(max_length=25)),
                ("password", models.CharField(max_length=25)),
                (
                    "phone_no",
                    models.CharField(
                        blank=True, default=None, max_length=15, null=True
                    ),
                ),
                (
                    "club_name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event.club",
                    ),
                ),
                (
                    "department_name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="event.department",
                    ),
                ),
            ],
        ),
    ]
