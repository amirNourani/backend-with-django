# Generated by Django 4.2.3 on 2023-07-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reservation_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='phone',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='person',
            field=models.IntegerField(default=1),
        ),
    ]