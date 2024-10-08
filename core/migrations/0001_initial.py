# Generated by Django 5.1 on 2024-08-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.PositiveIntegerField(help_text='ID do gênero no TMDb', unique=True)),
                ('name', models.CharField(help_text='Nome do gênero', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(default='', max_length=200)),
                ('imdb_id', models.CharField(blank=True, default='', max_length=200, unique=True)),
                ('tmdb_id', models.CharField(blank=True, default='', max_length=200, unique=True)),
                ('sinopse', models.TextField(blank=True)),
                ('duration', models.TimeField(blank=True, default='01:02:03')),
                ('trailer_url', models.URLField(blank=True, default='', null=True)),
                ('image_url', models.URLField()),
                ('thumb_url', models.URLField()),
                ('release_date', models.DateTimeField(blank=True)),
                ('votes', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('adult', models.BooleanField(default=False)),
                ('series', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('genres', models.ManyToManyField(related_name='%(class)ss', to='core.genre')),
            ],
        ),
    ]
