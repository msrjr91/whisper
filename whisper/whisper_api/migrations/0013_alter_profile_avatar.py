# Generated by Django 4.2 on 2023-04-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("whisper_api", "0012_profile_avatar_delete_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="Whisper/files/covers/default-avatar-profile-icon-of-social-media-user-vector.jpg",
                null=True,
                upload_to="",
            ),
        ),
    ]
