# Generated by Django 3.1.7 on 2021-03-11 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210307_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='client',
            new_name='profile',
        ),
    ]
