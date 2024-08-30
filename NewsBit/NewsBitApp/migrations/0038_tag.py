# Generated by Django 5.1 on 2024-08-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsBitApp', '0037_delete_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Entertainment', 'Entertainment'), ('Game', 'Game'), ('Travel', 'Travel'), ('LifeStyle', 'Lifestyle'), ('Tech', 'Tech'), ('Tour', 'Tour'), ('Health', 'Health'), ('Google', 'Google'), ('Fashion', 'Fashion'), ('Eyes', 'Eyes'), ('Hair', 'Hair'), ('Nail', 'Nail'), ('Lips', 'Lips')], default='Tech', max_length=50)),
            ],
        ),
    ]
