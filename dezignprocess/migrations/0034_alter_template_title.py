# Generated by Django 3.2.9 on 2021-11-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezignprocess', '0033_auto_20211122_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='title',
            field=models.CharField(default='placeholder', max_length=80, unique=True),
        ),
    ]
