# Generated by Django 4.2 on 2023-06-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0003_alter_post_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="file",
            field=models.FileField(upload_to=""),
        ),
    ]