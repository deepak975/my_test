# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('AccountNumber', models.IntegerField(max_length=30)),
                ('Location', models.CharField(max_length=30)),
            ],
        ),
    ]
