# Generated by Django 2.2.7 on 2019-11-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191119_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='タイトル'),
        ),
    ]
