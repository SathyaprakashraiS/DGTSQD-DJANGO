# Generated by Django 3.1.3 on 2021-02-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='img',
            field=models.ImageField(default='images/dlogo.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='img',
            field=models.ImageField(default='images/dlogo.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(default='images/dlogo.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='report',
            name='img',
            field=models.ImageField(default='images/dlogo.jpeg', upload_to='images'),
        ),
    ]