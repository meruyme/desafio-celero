# Generated by Django 3.2.3 on 2022-05-03 17:23

from django.db import migrations
from django.core.management import call_command


def load_command(apps, schema_editor):
    call_command("extract_noc_regions")


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_command)
    ]
