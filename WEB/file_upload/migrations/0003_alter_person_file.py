# Generated by Django 4.2 on 2023-06-21 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("file_upload", "0002_submit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="file",
            field=models.FileField(upload_to=""),
        ),
    ]
