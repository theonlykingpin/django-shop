# Generated by Django 4.2.4 on 2023-09-28 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0003_product_alter_productclass_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('buy_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('sale_price', models.PositiveBigIntegerField()),
                ('num_stock', models.PositiveIntegerField(default=0)),
                ('threshold_low_stack', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockrecords', to='catalog.product')),
            ],
        ),
    ]