# Generated by Django 3.2.15 on 2022-10-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
    ]