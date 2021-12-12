# Generated by Django 3.2.9 on 2021-12-12 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dezigntools', '0011_auto_20211212_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultquestion',
            name='age_range',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='age_range_set', to='dezigntools.agerange'),
        ),
        migrations.AlterField(
            model_name='defaultquestion',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gender_set', to='dezigntools.gender'),
        ),
        migrations.AlterField(
            model_name='defaultquestion',
            name='industry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='industry_set', to='dezigntools.industry'),
        ),
    ]