# Generated by Django 5.1.1 on 2024-11-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bloomerp", "0040_alter_userdetailviewtab_unique_together_and_more"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="filefolder",
            name="content_types",
            field=models.ManyToManyField(
                blank=True,
                help_text="Restrict folders to certain models.",
                null=True,
                to="contenttypes.contenttype",
                verbose_name="Models",
            ),
        ),
    ]
