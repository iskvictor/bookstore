# Generated by Django 2.1.4 on 2018-12-27 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181227_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Книга в заказе', 'verbose_name_plural': 'Книги  в заказе'},
        ),
    ]