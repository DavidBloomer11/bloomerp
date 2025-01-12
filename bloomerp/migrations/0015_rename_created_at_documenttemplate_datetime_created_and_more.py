# Generated by Django 5.1.1 on 2024-09-17 21:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bloomerp", "0014_alter_file_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="documenttemplate",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="documenttemplate",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.RenameField(
            model_name="documenttemplatefreevariable",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="documenttemplatefreevariable",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.RenameField(
            model_name="documenttemplateheader",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="documenttemplateheader",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.RenameField(
            model_name="kpi",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="kpi",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.RenameField(
            model_name="sqlquery",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="sqlquery",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.RenameField(
            model_name="sqlqueryfilter",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="sqlqueryfilter",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.RenameField(
            model_name="userkpidashboardviewpreference",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="userkpidashboardviewpreference",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.RenameField(
            model_name="userkpilistviewpreference",
            old_name="created_at",
            new_name="datetime_created",
        ),
        migrations.RenameField(
            model_name="userkpilistviewpreference",
            old_name="updated_at",
            new_name="datetime_updated",
        ),
        migrations.AddField(
            model_name="file",
            name="datetime_created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="file",
            name="datetime_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
