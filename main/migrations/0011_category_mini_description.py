# Generated by Django 5.0.1 on 2024-03-30 04:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_companydetails_facebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='mini_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]