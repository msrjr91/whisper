# Generated by Django 4.2 on 2023-04-16 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("whisper_api", "0026_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="/whisper/static/images/a-profile.jpg",
                max_length=300,
                null=True,
                upload_to="whisper/Whisper/static/images",
            ),
        ),
    ]