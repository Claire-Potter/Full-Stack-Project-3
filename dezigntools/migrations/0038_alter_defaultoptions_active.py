# Generated by Django 3.2.9 on 2021-12-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0037_auto_20211223_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultoptions',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
