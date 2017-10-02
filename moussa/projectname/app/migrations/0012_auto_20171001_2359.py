# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-01 23:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_doctor_exam_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='Date of exam')),
                ('Diagnosis', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('Doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance_Claim_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='Date of exam')),
                ('Amount', models.FloatField(default=0.0)),
                ('Status', models.CharField(choices=[('Filed', 'Filed'), ('Examining', 'Examining'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Paid', 'Paid')], max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('Medical_Administrator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Medical_Administrator_handling_claim_for_doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='Note Date')),
                ('Text', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Doctor_Correspondence_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('Doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL)),
                ('Notes', models.ManyToManyField(to='app.Note')),
            ],
        ),
        migrations.CreateModel(
            name='Raw_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=200)),
                ('File', models.FileField(upload_to='documents')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Results_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True, verbose_name='Date of exam')),
                ('Lab', models.CharField(max_length=200)),
                ('Notes', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('Doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='Record_Type',
            field=models.CharField(choices=[('Doctor Exam', 'Doctor Exam'), ('Test Result', 'Test Result'), ('Diagnosis', 'Diagnosis'), ('Insurance Claim', 'Insurance Claim'), ('Patient Doctor Correspondence', 'Patient Doctor Correspondence'), ('Raw', 'Raw')], default='Doctor Exam', max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor_exam_record',
            name='Doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='test_results_record',
            name='Record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Record'),
        ),
        migrations.AddField(
            model_name='raw_record',
            name='Record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Record'),
        ),
        migrations.AddField(
            model_name='patient_doctor_correspondence_record',
            name='Record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Record'),
        ),
        migrations.AddField(
            model_name='note',
            name='Patient_Doctor_Correspondence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Patient_Doctor_Correspondence_Record'),
        ),
        migrations.AddField(
            model_name='insurance_claim_record',
            name='Record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Record'),
        ),
        migrations.AddField(
            model_name='diagnosis_record',
            name='Record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Record'),
        ),
    ]