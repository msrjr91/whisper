# Generated by Django 4.2 on 2023-04-14 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("whisper_api", "0015_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-updated", "-created"]},
        ),
    ]
