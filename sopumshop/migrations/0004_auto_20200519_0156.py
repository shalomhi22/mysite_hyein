# Generated by Django 3.0.5 on 2020-05-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sopumshop', '0003_content_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='picture',
            field=models.ImageField(blank=True, upload_to='sopumshop/pic'),
        ),
    ]
