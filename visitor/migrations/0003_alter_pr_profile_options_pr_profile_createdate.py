# Generated by Django 5.0.2 on 2024-03-12 20:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_alter_pr_request_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pr_profile',
            options={'ordering': ['-createDate']},
        ),
        migrations.AddField(
            model_name='pr_profile',
            name='createDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]