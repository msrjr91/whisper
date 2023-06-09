# Generated by Django 4.2 on 2023-04-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("whisper_api", "0005_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="avatar.svg", null=True, upload_to="Whisper/static/images"
            ),
        ),
    ]
