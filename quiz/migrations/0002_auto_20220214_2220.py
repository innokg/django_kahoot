# Generated by Django 3.1 on 2022-02-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizzes',
            old_name='data_created',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='question',
            name='data_created',
        ),
        migrations.AddField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default='Asia/Bishkek', verbose_name='Date Created'),
            preserve_default=False,
        ),
    ]
