# Generated by Django 3.0.7 on 2020-06-10 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200611_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/category/', verbose_name='Изображение'),
        ),
    ]