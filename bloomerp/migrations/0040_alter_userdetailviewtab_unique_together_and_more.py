# Generated by Django 5.1.1 on 2024-10-30 23:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bloomerp", "0039_userdetailviewtab"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="userdetailviewtab",
            unique_together={("user", "link")},
        ),
        migrations.RemoveField(
            model_name="userdetailviewtab",
            name="content_type",
        ),
    ]
