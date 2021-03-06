# Generated by Django 2.2.5 on 2020-02-20 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artapp', '0006_remove_artwork1_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='more',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('age', models.IntegerField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
