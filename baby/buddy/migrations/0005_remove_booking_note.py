# Generated by Django 5.0.1 on 2024-01-09 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("buddy", "0004_remove_booking_datecheckin_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="note",
        ),
    ]
