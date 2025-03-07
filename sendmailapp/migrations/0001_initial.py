# Generated by Django 4.2 on 2025-01-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email_user', models.EmailField(max_length=254)),
                ('show_alternativ', models.CharField(choices=[('books', 'Books'), ('jobs', 'Jobs'), ('reviews', 'Reviews'), ('other', 'Other')], default='other')),
                ('descriptions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
