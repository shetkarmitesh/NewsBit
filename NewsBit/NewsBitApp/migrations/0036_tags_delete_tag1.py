# Generated by Django 5.1 on 2024-08-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0035_tag1_delete_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Tag1',
        ),
    ]
