# Generated by Django 2.2.4 on 2019-08-19 13:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("topics", "0042_auto_20190814_1600")]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="description",
            field=wagtail.core.fields.RichTextField(
                blank=True,
                default="",
                help_text="Optional short text description, max. 400 characters",
                max_length=400,
            ),
        )
    ]
