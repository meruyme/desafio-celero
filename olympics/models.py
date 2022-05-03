from django.db import models

from olympics.choices import Sex, Season, Medal


class Noc(models.Model):
    code = models.CharField(max_length=3)
    region = models.CharField(max_length=60)
    notes = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.code


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return f"{self.name} - {self.sport}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    noc = models.ForeignKey(Noc, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return f"{self.name} ({self.noc})"


class Games(models.Model):
    year = models.CharField(max_length=4)
    season = models.CharField(max_length=1, choices=Season.CHOICES)
    host_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return f"{self.year} {self.season}"


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=Sex.CHOICES)

    def __str__(self):
        return self.name


class AthleteGame(models.Model):
    age = models.IntegerField()
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='athletes')
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='athletes')
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='games')


class AthleteGameEvent(models.Model):
    athlete_game = models.ForeignKey(AthleteGame, on_delete=models.CASCADE, related_name='events')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='athlete_games')
    medal = models.CharField(max_length=1, choices=Medal.CHOICES)
