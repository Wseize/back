# Generated by Django 4.2.11 on 2024-06-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0023_remove_orderitem_suppliments'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='suppliments',
            field=models.ManyToManyField(blank=True, to='delivery.suppliment'),
        ),
    ]
