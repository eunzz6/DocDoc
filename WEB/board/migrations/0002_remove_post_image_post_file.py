# Generated by Django 4.2 on 2023-06-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image",
        ),
        migrations.AddField(
            model_name="post",
            name="file",
            field=models.FileField(default=2, upload_to=""),
            preserve_default=False,
        ),
    ]