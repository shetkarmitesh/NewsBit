# Generated by Django 5.1 on 2024-08-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0034_remove_tags_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
