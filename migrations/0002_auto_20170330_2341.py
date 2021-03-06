# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owaspcalc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='riskaudit',
            options={'ordering': ['-created_time_stamp']},
        ),
        migrations.AlterField(
            model_name='riskitemdetail',
            name='cat',
            field=models.CharField(choices=[('SKILL-LEVEL', 'Skill level'), ('MOTIVATION', 'Motivation'), ('OPPORTUNITY', 'Opportunity'), ('SIZE', 'Size'), ('EASE-OF-DISCOVERY', 'Ease of discovery'), ('EASE-OF-EXPLOIT', 'Ease of exploit'), ('AWARENESS', 'Awareness'), ('INTRUSION-DETECTION', 'Intrusion detection'), ('LOSS-OF-CONFIDENTIALTY', 'Loss of confidentiality'), ('LOSS-OF-INTEGRITY', 'Loss of integrity'), ('LOSS-OF-AVAILABILITY', 'Loss of availability'), ('LOSS-OF-ACCOUNTABILITY', 'Loss of accountability'), ('FINANCIAL-DAMAGE', 'Financial damage'), ('REPUTATION-DAMAGE', 'Reputation damage'), ('NON-COMPLIANCE', 'Non-compliance'), ('PRIVACY-VIOLATION', 'Privacy violation')], max_length=25),
        ),
    ]
