# Generated by Django 2.1.4 on 2019-02-16 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20190216_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='visual/')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('book', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
            options={
                'verbose_name_plural': 'Картинки слайдера',
                'verbose_name': 'Картинка слайдера',
            },
        ),
        migrations.RemoveField(
            model_name='bookimage',
            name='is_slider',
        ),
    ]
