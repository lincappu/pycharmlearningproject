# Generated by Django 3.2.8 on 2021-12-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='f', max_length=40, verbose_name='老师的姓')),
                ('last_name', models.CharField(default='ls', max_length=40, verbose_name='老师的名')),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'ter',
                'ordering': ['age'],
            },
        ),
    ]
