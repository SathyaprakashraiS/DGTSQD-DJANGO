# Generated by Django 3.1.3 on 2020-12-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201201_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='static/images/dlogo.jpeg', upload_to='images'),
        ),
    ]
