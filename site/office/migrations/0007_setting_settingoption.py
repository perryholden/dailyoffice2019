# Generated by Django 3.2.7 on 2021-11-27 22:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("office", "0006_holydayofficeday_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Setting",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=512)),
                ("description", models.TextField(blank=True, null=True)),
                ("order", models.PositiveSmallIntegerField(blank=True, null=True)),
                (
                    "setting_type",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Settings"), (2, "Additional Settings"), (3, "Expert Settings")], default=1
                    ),
                ),
                (
                    "site",
                    models.PositiveSmallIntegerField(choices=[(1, "Daily Office"), (2, "Family Prayer")], default=1),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SettingOption",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("order", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("value", models.CharField(max_length=255)),
                ("setting", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="office.setting")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
