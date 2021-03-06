# Generated by Django 2.2.9 on 2020-01-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='M.R.P.')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='M.R.P.')),
                ('description', models.CharField(max_length=256)),
                ('related_products', models.ManyToManyField(related_name='_product_related_products_+', to='product.Product')),
            ],
        ),
    ]
