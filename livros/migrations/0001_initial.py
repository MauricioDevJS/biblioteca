# Generated by Django 4.2.1 on 2023-05-03 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('release_year', models.DateField()),
                ('description', models.TextField()),
                ('created_at', models.DateField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]