# Generated by Django 3.2.9 on 2021-12-12 00:54

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0009_auto_20211212_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['image'],
            },
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_image', to='dezigntools.surveyimage'),
        ),
    ]