# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-01 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_doctor_nurse_system_administrator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Date',
        ),
        migrations.AddField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]