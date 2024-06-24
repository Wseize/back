# Generated by Django 4.2.11 on 2024-06-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0034_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Received', 'Received'), ('In Progress', 'In Progress'), ('In Transit', 'In Transit'), ('Complete', 'Complete'), ('Cancelled', 'Cancelled'), ('Confirmed', 'Confirmed')], default='Received', max_length=20),
        ),
    ]