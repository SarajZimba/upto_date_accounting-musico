# Generated by Django 4.0.6 on 2023-09-20 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_tblcrjournalentry_paidfrom_ledger_and_more'),
        ('product', '0007_product_cost_price_product_opening_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ledger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.accountledger'),
        ),
    ]
