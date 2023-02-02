# Generated by Django 3.2 on 2023-01-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b4', '0020_merge_20230129_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='uuid',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='background_photo',
            field=models.ImageField(null=True, upload_to='background'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='converte_photo',
            field=models.ImageField(null=True, upload_to='converte'),
        ),
    ]