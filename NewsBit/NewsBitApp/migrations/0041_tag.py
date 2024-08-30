# Generated by Django 5.1 on 2024-08-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0040_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Entertainment', 'danger'), ('Game', 'info'), ('Travel', 'primary'), ('LifeStyle', 'success'), ('Tech', 'danger')], default='Tech', max_length=50)),
            ],
        ),
    ]
