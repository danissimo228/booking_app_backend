# Generated by Django 5.0.2 on 2024-03-30 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_sub_subs_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='photo_url',
            new_name='photo',
        ),
    ]