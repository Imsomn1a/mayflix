# Generated by Django 5.1 on 2024-08-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tag',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
