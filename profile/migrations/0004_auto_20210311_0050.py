# Generated by Django 3.1.7 on 2021-03-11 03:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210311_0050'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile', '0003_auto_20210304_2308'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Profile',
        ),
    ]
