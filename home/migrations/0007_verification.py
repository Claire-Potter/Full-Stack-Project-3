# Generated by Django 3.2.9 on 2021-12-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification', models.CharField(max_length=250)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['updated_on'],
                'get_latest_by': ['updated_on'],
            },
        ),
    ]