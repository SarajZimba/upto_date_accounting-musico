# Generated by Django 4.0.6 on 2025-01-23 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlysalaryreport',
            name='month',
        ),
        migrations.RemoveField(
            model_name='monthlysalaryreport',
            name='nepali_date',
        ),
        migrations.RemoveField(
            model_name='monthlysalaryreport',
            name='nepali_year',
        ),
    ]
