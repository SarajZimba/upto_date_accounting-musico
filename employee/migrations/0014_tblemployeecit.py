# Generated by Django 4.0.6 on 2025-01-31 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_tblemployeecommision'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblEmployeeCIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('sorting_order', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('empID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
