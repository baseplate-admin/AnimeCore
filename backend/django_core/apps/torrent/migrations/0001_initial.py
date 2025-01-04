# Generated by Django 5.1.4 on 2025-01-04 23:27

import django.db.models.deletion
import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Torrent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_default=django.db.models.functions.datetime.Now())),
                ('name', models.TextField()),
                ('info_hash', models.CharField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.PositiveIntegerField()),
                ('is_seeding', models.BooleanField()),
                ('peer_id', models.TextField()),
                ('torrent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peers', to='torrent.torrent')),
            ],
            options={
                'unique_together': {('torrent', 'ip', 'port', 'peer_id')},
            },
        ),
    ]
