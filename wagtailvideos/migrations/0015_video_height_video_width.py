# Generated by Django 4.2.13 on 2024-05-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailvideos", "0014_alter_videotrack_file_alter_videotrack_kind_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="height",
            field=models.IntegerField(editable=False, null=True, verbose_name="height"),
        ),
        migrations.AddField(
            model_name="video",
            name="width",
            field=models.IntegerField(editable=False, null=True, verbose_name="width"),
        ),
    ]
