# Generated by Django 2.2.10 on 2020-11-27 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0027_auto_20201126_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='is_active',
            new_name='is_highlighted',
        ),
    ]
