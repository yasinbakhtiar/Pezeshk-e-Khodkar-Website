# Generated by Django 4.0.2 on 2023-05-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_result_image_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='image_format',
            field=models.CharField(max_length=64),
        ),
    ]