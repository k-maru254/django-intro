# Generated by Django 4.2.6 on 2023-11-10 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject_code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(default='', max_length=10)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('sir_name', models.CharField(max_length=20)),
                ('tac_number', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('employment_date', models.DateField(default=datetime.date.today)),
                ('subjects', models.ManyToManyField(to='base.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=5)),
                ('admission_no', models.IntegerField(null=True)),
                ('admissionDate', models.DateField(auto_now=True)),
                ('subjects', models.ManyToManyField(to='base.subject')),
            ],
        ),
    ]
