# Generated by Django 4.2.11 on 2024-06-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0032_store_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='address',
        ),
        migrations.AddField(
            model_name='store',
            name='governorate',
            field=models.CharField(choices=[('sbeitla', 'Sbeitla'), ('feriana', 'Feriana'), ('thala', 'Thala')], default='sbeitla', max_length=20),
        ),
        migrations.AlterField(
            model_name='store',
            name='country',
            field=models.CharField(choices=[('kasserine', 'Kasserine'), ('mahdia', 'Mahdia')], default='kasserine', max_length=20),
        ),
    ]
