# Generated by Django 5.0.1 on 2024-01-08 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("buddy", "0002_alter_booking_adults_alter_booking_children_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="adults",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="children",
        ),
    ]
