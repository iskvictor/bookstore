# Generated by Django 2.1.4 on 2019-02-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20190209_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcategory',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=128, null=True, unique=True),
        ),
    ]
