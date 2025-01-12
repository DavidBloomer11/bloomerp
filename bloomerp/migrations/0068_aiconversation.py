# Generated by Django 5.1.1 on 2025-01-11 00:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bloomerp", "0067_alter_todo_required_by"),
    ]

    operations = [
        migrations.CreateModel(
            name="AIConversation",
            fields=[
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("datetime_updated", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(default="AI Conversation", max_length=255)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("conversation_history", models.JSONField()),
                (
                    "conversation_type",
                    models.CharField(
                        choices=[
                            ("sql", "SQL"),
                            ("document_template", "Document Template Generator"),
                            ("tiny_mce_content", "TinyMCE Content Generator"),
                            ("bloom_ai", "Bloom AI"),
                            ("code", "Code Generator"),
                        ],
                        default="bloom_ai",
                        max_length=20,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "AI conversation",
                "verbose_name_plural": "AI conversations",
                "db_table": "bloomerp_ai_conversation",
                "managed": True,
            },
        ),
    ]
