# Generated by Django 4.0.6 on 2025-01-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_organization_noofpaidleavesallowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='dashain_month',
            field=models.CharField(choices=[('Baishakh', 'Baishakh'), ('Jestha', 'Jestha'), ('Asar', 'Asar'), ('Shrawan', 'Shrawan'), ('Bhadau', 'Bhadau'), ('Aswin', 'Aswin'), ('Kartik', 'Kartik'), ('Mangsir', 'Mangsir'), ('Poush', 'Poush'), ('Magh', 'Magh'), ('Falgun', 'Falgun'), ('Chaitra', 'Chaitra')], default='Baishakh', max_length=20),
        ),
    ]
