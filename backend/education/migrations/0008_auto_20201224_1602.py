# Generated by Django 3.1.3 on 2020-12-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0007_auto_20201224_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='contents',
            field=models.TextField(blank=True, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='curriculum',
            name='subject',
            field=models.TextField(verbose_name='주제'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='contents',
            field=models.TextField(blank=True, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='effect',
            field=models.CharField(blank=True, max_length=100, verbose_name='기대효과'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='goal',
            field=models.CharField(blank=True, max_length=100, verbose_name='학습목표'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='main_contents',
            field=models.CharField(blank=True, max_length=100, verbose_name='주요 컨텐츠'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='method',
            field=models.TextField(blank=True, verbose_name='학습방법'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='contents',
            field=models.TextField(blank=True, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='outline',
            field=models.CharField(blank=True, max_length=100, verbose_name='개요'),
        ),
    ]