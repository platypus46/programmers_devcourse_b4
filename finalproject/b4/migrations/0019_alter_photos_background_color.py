# Generated by Django 4.1.5 on 2023-01-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("b4", "0018_alter_photos_background_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photos",
            name="background_color",
            field=models.CharField(default="#ffffff", max_length=10),
        ),
    ]
