# Generated by Django 2.2.5 on 2020-02-19 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0005_auto_20200219_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork1',
            name='desc',
        ),
    ]
