# Generated by Django 4.2 on 2023-04-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("whisper_api", "0004_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(default="avatar.svg", null=True, upload_to=""),
        ),
    ]
