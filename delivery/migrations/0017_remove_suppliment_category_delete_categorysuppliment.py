# Generated by Django 4.2.11 on 2024-06-04 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0016_categorysuppliment_suppliment_item_suppliments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliment',
            name='category',
        ),
        migrations.DeleteModel(
            name='CategorySuppliment',
        ),
    ]