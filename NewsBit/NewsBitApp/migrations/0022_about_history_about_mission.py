# Generated by Django 5.1 on 2024-09-18 08:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0021_about_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='history',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='mission',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
