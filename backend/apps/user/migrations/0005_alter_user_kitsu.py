# Generated by Django 4.0.4 on 2022-05-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_kitsu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="kitsu",
            field=models.JSONField(default=dict),
        ),
    ]
