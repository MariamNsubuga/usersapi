# Generated by Django 4.2.7 on 2023-11-03 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Admins',
        ),
    ]