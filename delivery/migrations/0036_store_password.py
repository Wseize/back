# Generated by Django 4.2.11 on 2024-06-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0035_order_latitude_order_longitude_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='password',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]