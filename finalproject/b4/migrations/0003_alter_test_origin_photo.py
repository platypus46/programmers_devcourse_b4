# Generated by Django 4.0.3 on 2023-01-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b4', '0002_alter_test_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='origin_photo',
            field=models.ImageField(null=True, upload_to='origin'),
        ),
    ]
