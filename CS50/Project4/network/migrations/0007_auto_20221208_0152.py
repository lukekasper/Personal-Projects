# Generated by Django 3.2.15 on 2022-12-08 01:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20221207_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Relations',
        ),
    ]
