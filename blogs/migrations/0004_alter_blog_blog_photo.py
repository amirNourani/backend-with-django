# Generated by Django 4.0 on 2022-01-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_blog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_photo',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]