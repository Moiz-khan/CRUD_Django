# Generated by Django 3.2.3 on 2021-06-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='AM_PM_db',
            field=models.CharField(default='AM/PM', max_length=100),
        ),
    ]
