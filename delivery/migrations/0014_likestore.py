# Generated by Django 4.2.11 on 2024-06-03 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0013_alter_ratingstore_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='delivery.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'store')},
            },
        ),
    ]