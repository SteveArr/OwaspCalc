# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('details', models.TextField()),
                ('created_time_stamp', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiskItemDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('score', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('cat', models.CharField(choices=[('SKILL-LEVEL', 'Skill level'), ('MOTIVATION', 'Motivation'), ('OPPORTUNITY', 'Opportunity'), ('SIZE', 'Size')], max_length=16)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='riskaudit',
            name='motivation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='owaspcalc.RiskItemDetail'),
        ),
        migrations.AddField(
            model_name='riskaudit',
            name='opportunity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='owaspcalc.RiskItemDetail'),
        ),
        migrations.AddField(
            model_name='riskaudit',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='owaspcalc.RiskItemDetail'),
        ),
        migrations.AddField(
            model_name='riskaudit',
            name='skill_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='owaspcalc.RiskItemDetail'),
        ),
    ]
