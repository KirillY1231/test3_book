# Generated by Django 3.1.3 on 2021-02-24 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('sname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Сылка')),
                ('phone', models.CharField(max_length=100, verbose_name='Имя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Фото')),
                ('address', models.ForeignKey(blank=True, help_text='Адрес', null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.address')),
            ],
        ),
    ]
