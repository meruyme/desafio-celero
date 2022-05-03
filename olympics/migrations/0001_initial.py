# Generated by Django 3.2.3 on 2022-05-03 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='AthleteGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('height', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='olympics.athlete')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Noc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('region', models.CharField(max_length=60)),
                ('notes', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('noc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='olympics.noc')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('season', models.CharField(choices=[('1', 'Winter'), ('2', 'Summer')], max_length=1)),
                ('host_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='olympics.city')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='olympics.sport')),
            ],
        ),
        migrations.CreateModel(
            name='AthleteGameEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal', models.CharField(choices=[('1', 'Gold'), ('2', 'Silver'), ('3', 'Bronze')], max_length=1)),
                ('athlete_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='olympics.athletegame')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athlete_games', to='olympics.event')),
            ],
        ),
        migrations.AddField(
            model_name='athletegame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athletes', to='olympics.games'),
        ),
        migrations.AddField(
            model_name='athletegame',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athletes', to='olympics.team'),
        ),
    ]
