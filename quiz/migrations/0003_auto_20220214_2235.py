# Generated by Django 3.1 on 2022-02-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20220214_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Last Updated'),
        ),
    ]
