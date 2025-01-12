# Generated by Django 5.1.1 on 2025-01-08 00:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bloomerp", "0064_remove_todo_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="priority",
            field=models.IntegerField(
                choices=[(1, "Low"), (2, "Medium"), (3, "High")],
                default=2,
                help_text="The priority of the todo",
            ),
        ),
        migrations.AlterField(
            model_name="todo",
            name="required_by",
            field=models.DateTimeField(
                blank=True,
                help_text="The date by which the todo is required",
                null=True,
            ),
        ),
    ]
