# Generated by Django 5.1.1 on 2024-11-20 17:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bloomerp", "0047_rename_comment_comment_content_remove_comment_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userlistviewpreference",
            name="is_main",
        ),
    ]
