# Generated by Django 2.2 on 2019-08-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzasize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('medium_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
    ]
