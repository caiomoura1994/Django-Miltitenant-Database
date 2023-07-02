# Generated by Django 3.2.19 on 2023-07-01 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_auto_20230624_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='stripe_customer_id',
            field=models.CharField(default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
