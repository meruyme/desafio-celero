# Generated by Django 3.2.3 on 2022-05-05 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0005_auto_20220505_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noc',
            old_name='code',
            new_name='id',
        ),
    ]
