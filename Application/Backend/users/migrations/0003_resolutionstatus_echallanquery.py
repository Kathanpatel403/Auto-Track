# Generated by Django 5.0.6 on 2025-01-26 16:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_otpverification'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResolutionStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20, unique=True, verbose_name='Status')),
                ('description', models.TextField(verbose_name='Status Description')),
            ],
        ),
        migrations.CreateModel(
            name='EchallanQuery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('query_description', models.TextField(verbose_name='Query Description')),
                ('query_date', models.DateTimeField(auto_now_add=True, verbose_name='Query Date')),
                ('issue_type', models.TextField(verbose_name='Issue Type')),
                ('document_url', models.TextField(verbose_name='Document URL')),
                ('resolution_details', models.TextField(blank=True, null=True, verbose_name='Resolution Details')),
                ('resolved_at', models.DateTimeField(blank=True, null=True, verbose_name='Resolved At')),
                ('echallan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queries', to='users.echallan_main', verbose_name='E-Challan')),
                ('resolved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resolved_queries', to=settings.AUTH_USER_MODEL, verbose_name='Resolved By (Admin)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queries', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('resolution_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='users.resolutionstatus', verbose_name='Resolution Status')),
            ],
        ),
    ]
