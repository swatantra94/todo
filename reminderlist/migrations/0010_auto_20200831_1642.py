# Generated by Django 3.1 on 2020-08-31 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminderlist', '0009_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='like',
            new_name='likes',
        ),
    ]
