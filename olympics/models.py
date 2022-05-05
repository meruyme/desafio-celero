from django.db import models

from olympics.choices import Sex, Season, Medal


class Noc(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    region = models.CharField(max_length=60)
    notes = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.id


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.name} - {self.sport}"

    class Meta:
        unique_together = ('name', 'sport')


class Team(models.Model):
    name = models.CharField(max_length=255)
    noc = models.ForeignKey(Noc, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return f"{self.name} {self.noc}"

    class Meta:
        unique_together = ('name', 'noc')


class Games(models.Model):
    year = models.CharField(max_length=4)
    season = models.CharField(max_length=1, choices=Season.CHOICES)
    host_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='games')

    class Meta:
        unique_together = ('year', 'season')

    def __str__(self):
        return f"{self.year} {self.get_season_display()}"


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=Sex.CHOICES)

    def __str__(self):
        return self.name


class AthleteGame(models.Model):
    age = models.IntegerField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='athletes')
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='athletes')
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='games')

    class Meta:
        unique_together = ('team', 'game', 'athlete')


class AthleteGameEvent(models.Model):
    athlete_game = models.ForeignKey(AthleteGame, on_delete=models.CASCADE, related_name='events')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='athlete_games')
    medal = models.CharField(max_length=1, choices=Medal.CHOICES, null=True)

    class Meta:
        unique_together = ('athlete_game', 'event')
