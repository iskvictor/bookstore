# Generated by Django 2.1.4 on 2019-01-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='shot_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]