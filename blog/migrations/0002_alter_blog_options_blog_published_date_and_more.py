# Generated by Django 5.1.1 on 2024-10-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={},
        ),
        migrations.AddField(
            model_name="blog",
            name="published_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
