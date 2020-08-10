# Generated by Django 3.1 on 2020-08-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reminderlist', '0005_delete_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
            ],
        ),
    ]