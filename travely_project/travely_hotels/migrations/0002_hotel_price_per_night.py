# Generated by Django 4.2.8 on 2024-01-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travely_hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='price_per_night',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]