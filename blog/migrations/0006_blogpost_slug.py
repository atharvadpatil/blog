# Generated by Django 3.1.4 on 2021-01-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='first'),
            preserve_default=False,
        ),
    ]
