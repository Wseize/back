# Generated by Django 4.2.11 on 2024-06-07 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0029_item_souscategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='souscategory',
        ),
        migrations.DeleteModel(
            name='SousCategory',
        ),
    ]
