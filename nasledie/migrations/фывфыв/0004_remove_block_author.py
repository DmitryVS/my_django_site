# Generated by Django 3.0.6 on 2020-05-21 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nasledie', '0003_block_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='author',
        ),
    ]
