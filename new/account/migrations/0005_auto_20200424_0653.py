# Generated by Django 3.0.5 on 2020-04-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200423_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='email'),
        ),
    ]
