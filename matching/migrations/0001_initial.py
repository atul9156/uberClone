# Generated by Django 5.0.6 on 2024-05-27 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "cab_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.cab"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.passenger"
                    ),
                ),
            ],
            options={
                "db_table": "trips",
                "indexes": [
                    models.Index(
                        fields=["is_completed"], name="trips_is_comp_872d14_idx"
                    )
                ],
            },
        ),
    ]
