# Generated by Django 2.2.5 on 2020-02-22 13:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artapp', '0011_auto_20200222_1846'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='more1',
            new_name='more2',
        ),
    ]