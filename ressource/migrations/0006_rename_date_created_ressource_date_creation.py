# Generated by Django 4.2.2 on 2023-10-17 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ressource', '0005_ressource_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ressource',
            old_name='date_created',
            new_name='date_creation',
        ),
    ]
