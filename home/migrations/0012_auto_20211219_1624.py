# Generated by Django 3.2.9 on 2021-12-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20211217_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='do_not_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='home',
            name='do_not_delete',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='verification',
            name='do_not_delete',
            field=models.BooleanField(default=True),
        ),
    ]
