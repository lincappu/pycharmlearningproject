# Generated by Django 3.2.8 on 2021-12-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0004_author_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='phone',
            field=models.IntegerField(default=None),
        ),
    ]
