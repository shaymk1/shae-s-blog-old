# Generated by Django 5.0.1 on 2024-02-08 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_post_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="sub_title",
            new_name="category",
        ),
    ]
