# Generated by Django 3.0.7 on 2020-06-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200611_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='email',
        ),
        migrations.AddField(
            model_name='manager',
            name='chat_id',
            field=models.IntegerField(null=True, verbose_name='Чат id telegram'),
        ),
    ]
