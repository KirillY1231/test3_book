# Generated by Django 3.1.3 on 2021-02-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20210225_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='home',
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='person',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дом'),
        ),
    ]
