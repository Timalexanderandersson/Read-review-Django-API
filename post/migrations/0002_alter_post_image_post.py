# Generated by Django 5.1.3 on 2024-11-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_post',
            field=models.ImageField(default='book-front-page_rt7nvr', upload_to='images/'),
        ),
    ]
