# Generated by Django 3.2.9 on 2021-12-27 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0038_alter_defaultoptions_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='defaultanswers',
            options={'ordering': ['survey'], 'verbose_name_plural': 'Default Answers'},
        ),
        migrations.RemoveField(
            model_name='defaultanswers',
            name='submission',
        ),
    ]
