# Generated by Django 5.1.3 on 2025-01-04 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torrent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peer',
            old_name='last_seen',
            new_name='updated_at',
        ),
    ]
