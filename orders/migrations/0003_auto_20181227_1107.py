# Generated by Django 2.1.4 on 2018-12-27 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181222_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]
