# Generated by Django 3.2.3 on 2021-06-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0002_registration_am_pm_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phoneNo_db',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='registration',
            name='time_db',
            field=models.CharField(max_length=100),
        ),
    ]
