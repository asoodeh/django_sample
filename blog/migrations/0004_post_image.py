# Generated by Django 4.1 on 2024-04-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/img/default.jpg', upload_to='blog/img/'),
        ),
    ]
