# Generated by Django 3.2.15 on 2022-12-09 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20221209_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='user',
            new_name='prof_user',
        ),
    ]
