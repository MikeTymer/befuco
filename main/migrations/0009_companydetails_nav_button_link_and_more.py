# Generated by Django 5.0.1 on 2024-03-30 04:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_companydetails_embedded_video_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='nav_button_link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companydetails',
            name='nav_button_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]