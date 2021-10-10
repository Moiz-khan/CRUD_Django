# Generated by Django 3.2.3 on 2021-06-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('aid_db', models.AutoField(primary_key=True, serialize=False)),
                ('patientName_db', models.CharField(max_length=100)),
                ('phoneNo_db', models.IntegerField()),
                ('doctorName', models.CharField(max_length=100)),
                ('specialist_db', models.CharField(max_length=100)),
                ('day_db', models.CharField(max_length=100)),
                ('time_db', models.TimeField(max_length=100)),
                ('fees_db', models.IntegerField()),
                ('tokenNo_db', models.IntegerField()),
            ],
        ),
    ]
