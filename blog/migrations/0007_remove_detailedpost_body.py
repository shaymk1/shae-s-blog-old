# Generated by Django 5.0.1 on 2024-02-13 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_tag_detailedpost"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="detailedpost",
            name="body",
        ),
    ]
