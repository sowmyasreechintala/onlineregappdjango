# Generated by Django 3.0.5 on 2020-07-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminnModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('Coursename', models.CharField(max_length=50, unique=True)),
                ('Faculty', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.CharField(max_length=50)),
                ('Fee', models.IntegerField()),
                ('Duration', models.CharField(max_length=100)),
            ],
        ),
    ]
