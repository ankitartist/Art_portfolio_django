# Generated by Django 2.2.5 on 2020-02-23 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0018_artwork1_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork1',
            name='type',
        ),
    ]
