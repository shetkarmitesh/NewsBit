# Generated by Django 5.1 on 2024-09-02 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0063_author_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='posts',
        ),
    ]
