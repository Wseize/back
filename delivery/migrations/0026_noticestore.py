# Generated by Django 4.2.11 on 2024-06-05 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0025_remove_orderitem_suppliments'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notices', to='delivery.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
