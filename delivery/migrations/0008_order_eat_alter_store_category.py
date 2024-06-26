# Generated by Django 4.2.11 on 2024-06-02 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_store_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='eat',
            field=models.CharField(choices=[('delivery', 'delivery'), ('take_out', 'take_out'), ('on_the_spot', 'on_the_spot')], default='delivery', max_length=20),
        ),
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='delivery.typecategory'),
        ),
    ]
