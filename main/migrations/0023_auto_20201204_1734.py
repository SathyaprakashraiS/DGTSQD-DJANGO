# Generated by Django 3.1.2 on 2020-12-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='img',
            field=models.ImageField(default='static/images/14358.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(default='static/images/14358.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(default='static/images/14358.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(default='static/images/14358.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='report',
            name='img',
            field=models.ImageField(default='static/images/14358.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='static/images/14358.jpg', upload_to='images'),
        ),
    ]