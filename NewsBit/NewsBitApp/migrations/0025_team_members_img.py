# Generated by Django 5.1 on 2024-09-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0024_team_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_members',
            name='img',
            field=models.ImageField(default=1, upload_to='teams'),
            preserve_default=False,
        ),
    ]
