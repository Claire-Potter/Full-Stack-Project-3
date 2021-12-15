# Generated by Django 3.2.9 on 2021-12-15 15:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0048_auto_20211215_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
