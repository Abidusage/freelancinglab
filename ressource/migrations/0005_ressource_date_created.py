# Generated by Django 4.2.2 on 2023-10-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressource', '0004_alter_ressource_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressource',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]