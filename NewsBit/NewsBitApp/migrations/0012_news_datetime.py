# Generated by Django 5.1 on 2024-08-27 10:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0011_news_tagbackcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
