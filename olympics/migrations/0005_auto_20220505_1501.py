# Generated by Django 3.2.3 on 2022-05-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympics', '0004_alter_athletegame_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noc',
            name='id',
        ),
        migrations.AlterField(
            model_name='noc',
            name='code',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]