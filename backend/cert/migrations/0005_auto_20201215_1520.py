# Generated by Django 3.1.3 on 2020-12-15 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0004_auto_20201215_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='customgroup',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='group_name'),
        ),
    ]
