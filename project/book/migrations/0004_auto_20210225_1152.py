# Generated by Django 3.1.3 on 2021-02-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210225_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]