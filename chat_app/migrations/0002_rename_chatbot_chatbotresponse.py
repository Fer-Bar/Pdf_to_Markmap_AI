# Generated by Django 5.1.6 on 2025-02-25 16:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat_app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ChatBot",
            new_name="ChatBotResponse",
        ),
    ]
