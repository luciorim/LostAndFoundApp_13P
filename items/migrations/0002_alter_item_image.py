# Generated by Django 5.1.6 on 2025-02-27 18:53

import items.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to=items.utils.item_image_path),
        ),
    ]
