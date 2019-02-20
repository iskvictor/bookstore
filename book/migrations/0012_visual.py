# Generated by Django 2.1.4 on 2019-02-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20190216_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('image', models.ImageField(upload_to='visual/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'картинки для слайдера',
                'verbose_name': 'картинка для слайдера',
            },
        ),
    ]
