# Generated by Django 5.0.2 on 2024-05-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0007_remove_pr_profile_passportid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pr_profile',
            name='personalPhoto',
            field=models.ImageField(default='', upload_to='personalPhoto'),
        ),
    ]