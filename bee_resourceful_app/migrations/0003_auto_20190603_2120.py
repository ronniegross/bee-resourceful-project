# Generated by Django 2.2.2 on 2019-06-03 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee_resourceful_app', '0002_auto_20190603_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='resource_number',
            new_name='resource_phone_number',
        ),
    ]
