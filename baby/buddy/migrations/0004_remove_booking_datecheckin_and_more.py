# Generated by Django 5.0.1 on 2024-01-09 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("buddy", "0003_remove_booking_adults_remove_booking_children"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="datecheckin",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="datecheckout",
        ),
    ]