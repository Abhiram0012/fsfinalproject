# Generated by Django 5.0.1 on 2024-01-09 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("buddy", "0006_booking_note"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="booking",
            table="Booking",
        ),
    ]