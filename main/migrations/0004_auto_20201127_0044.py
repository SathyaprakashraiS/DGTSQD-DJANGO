# Generated by Django 3.1.3 on 2020-11-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201127_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='info',
            field=models.CharField(max_length=1000),
        ),
    ]
