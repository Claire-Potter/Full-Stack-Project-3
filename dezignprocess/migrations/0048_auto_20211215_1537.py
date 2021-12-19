# Generated by Django 3.2.9 on 2021-12-15 15:37

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0047_auto_20211215_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Featured', 'Featured'), ('Step', 'Step'), ('Tool', 'Tool'), ('Other', 'Other')], default='Other', max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Images',
                'ordering': ['category'],
                'get_latest_by': ['added'],
            },
        ),
        migrations.AlterField(
            model_name='resource',
            name='video_name',
            field=models.CharField(blank=True, default='placeholder', max_length=200),
        ),
    ]