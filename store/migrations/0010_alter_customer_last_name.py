# Generated by Django 3.2.5 on 2021-08-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_customer_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
