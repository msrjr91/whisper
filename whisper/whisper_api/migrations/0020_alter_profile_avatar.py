# Generated by Django 4.2 on 2023-04-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("whisper_api", "0019_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="/Users/michaelross/Desktop/GA/SEIR123/whisper/whisper/files/covers/default-avatar-profile-icon-of-social-media-user-vector.jpg",
                max_length=300,
                null=True,
                upload_to="whisper/static/images",
            ),
        ),
    ]
