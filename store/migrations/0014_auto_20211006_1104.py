# Generated by Django 3.2.5 on 2021-10-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_order_satuts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='satuts',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
