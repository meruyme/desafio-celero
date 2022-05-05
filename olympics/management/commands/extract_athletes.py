from django.core.management.base import BaseCommand
from django.db import transaction

from olympics.choices import Season, Medal
from olympics.models import Noc, Athlete, Games, City, Sport, Event, Team, AthleteGame, AthleteGameEvent
import csv
import os

from olympics.utils import get_id


class Command(BaseCommand):
    help = 'Extract athletes and events from csv file'
    h = {
        "ID": 0, "Name": 1, "Sex": 2, "Age": 3, "Height": 4, "Weight": 5, "Team": 6, "NOC": 7,
        "Games": 8, "Year": 9, "Season": 10, "City": 11, "Sport": 12, "Event": 13, "Medal": 14
    }

    quantity_bulk = 10000

    @transaction.atomic()
    def handle(self, *args, **options):
        try:
            path = os.path.join('olympics', 'management', 'athlete_events.csv')
            empty_values = ['NA']
            # Processing AthleteGame with bulk_create
            print('Processing AthleteGame...')
            with open(path, "r") as csv_file:
                df = csv.reader(csv_file, delimiter=",")
                next(df)
                athletes = {athlete.name: athlete for athlete in Athlete.objects.all()}
                nocs = {noc.code: noc for noc in Noc.objects.all()}
                cities = {city.name: city for city in City.objects.all()}
                games = {f"{game.year} {game.season}": game for game in Games.objects.all()}
                sports = {sport.name: sport for sport in Sport.objects.all()}
                events = {event.name: event for event in Event.objects.all()}
                teams = {f"{team.name} {team.noc}": team for team in Team.objects.all()}
                athletes_games = {f"{athlete_game.athlete} {athlete_game.team} {athlete_game.game}": athlete_game
                                  for athlete_game in AthleteGame.objects.all()}
                athletes_games_aux = athletes_games.copy()
                data = []
                for row in df:
                    season = get_id(Season, row[self.h['Season']]) if row[self.h['Season']] not in empty_values \
                        else None
                    noc = nocs.get(row[self.h['NOC']])
                    athlete = athletes.get(row[self.h['Name']])
                    city = cities.get(row[self.h['City']])
                    game = games.get(row[self.h['Games']])
                    sport = sports.get(row[self.h['Sport']])
                    event = events.get(row[self.h['Event']])
                    team = teams.get(f"{row[self.h['Team']]} {row[self.h['NOC']]}")
                    name_item = f"{row[self.h['Name']]} {row[self.h['Team']]} {row[self.h['NOC']]} " \
                                f"{row[self.h['Games']]}"
                    if not athletes_games_aux.get(name_item):
                        if not athlete:
                            athlete = Athlete.objects.create(name=row[self.h['Name']], sex=row[self.h['Sex']])
                            athletes[athlete.name] = athlete
                        if not city:
                            city = City.objects.create(name=row[self.h['City']])
                            cities[city.name] = city
                        if not game:
                            game = Games.objects.create(year=row[self.h['Year']], season=season, host_city=city)
                            games[f"{game.year} {game.season}"] = game
                        if not sport:
                            sport = Sport.objects.create(name=row[self.h['Sport']])
                            sports[sport.name] = sport
                        if not event:
                            event = Event.objects.create(name=row[self.h['Event']], sport=sport)
                            events[event.name] = event
                        if not team:
                            team = Team.objects.create(name=row[self.h['Team']], noc=noc)
                            teams[f"{team.name} {team.noc}"] = team
                        athletes_games_aux[name_item] = True
                        age = row[self.h['Age']] if row[self.h['Age']] not in empty_values else None
                        height = row[self.h['Height']] if row[self.h['Height']] not in empty_values else None
                        weight = row[self.h['Weight']] if row[self.h['Weight']] not in empty_values else None
                        data.append(AthleteGame(age=age, height=height,
                                                weight=weight,
                                                team=team, game=game, athlete=athlete))
                        if len(data) > self.quantity_bulk:
                            objs = AthleteGame.objects.bulk_create(data)
                            athletes_games.update(
                                {f"{athlete_game.athlete} {athlete_game.team} {athlete_game.game}": athlete_game
                                 for athlete_game in objs}
                            )
                            data = []
                if data:
                    objs = AthleteGame.objects.bulk_create(data)
                    athletes_games.update(
                        {f"{athlete_game.athlete} {athlete_game.team} {athlete_game.game}": athlete_game
                         for athlete_game in objs}
                    )

                # Processing AthleteGameEvent with bulk_create
                print('Processing AthleteGameEvent...')
                csv_file.seek(0)
                df = csv.reader(csv_file, delimiter=",")
                next(df)
                data = []
                for row in df:
                    medal = get_id(Medal, row[self.h['Medal']]) if row[self.h['Medal']] not in empty_values \
                        else None
                    event = events.get(row[self.h['Event']])
                    name_item = f"{row[self.h['Name']]} {row[self.h['Team']]} {row[self.h['NOC']]} " \
                                f"{row[self.h['Games']]}"
                    athlete_game = athletes_games.get(name_item)
                    data.append(AthleteGameEvent(athlete_game=athlete_game, event=event, medal=medal))
                    if len(data) > self.quantity_bulk:
                        AthleteGameEvent.objects.bulk_create(data)
                        data = []
                if data:
                    AthleteGameEvent.objects.bulk_create(data)
                print("OK!")

        except Exception as e:
            print(e)
