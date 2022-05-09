from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

from olympics.models import City, Sport, Team, Games, Athlete, Event, AthleteGame, AthleteGameEvent
from olympics.serializers import CitySerializer, SportSerializer, TeamSerializer, ReadTeamSerializer, GamesSerializer, \
    AthleteSerializer, EventSerializer, AthleteGameSerializer, AthleteGameEventSerializer, ReadGamesSerializer, \
    ReadAthleteSerializer, ReadEventSerializer, ReadAthleteGameSerializer, ReadAthleteGameEventSerializer


class CityList(generics.ListCreateAPIView):
    model = City
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.all()
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('name', openapi.IN_QUERY,
                                                              description="City's name",
                                                              type=openapi.TYPE_STRING, required=False)])
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SportList(generics.ListCreateAPIView):
    model = Sport
    serializer_class = SportSerializer

    def get_queryset(self):
        queryset = Sport.objects.all()
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('name', openapi.IN_QUERY,
                                                              description="Sport's name",
                                                              type=openapi.TYPE_STRING, required=False)])
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class TeamList(generics.ListCreateAPIView):
    model = Team
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all()
        name = self.request.query_params.get('name')
        noc = self.request.query_params.get('noc')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if noc:
            queryset = queryset.filter(noc__pk=noc)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('name', openapi.IN_QUERY,
                                                              description="Team's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('noc', openapi.IN_QUERY,
                                                              description="NOC three-letter code",
                                                              type=openapi.TYPE_STRING, required=False),
                                            ],
                         responses={status.HTTP_200_OK: openapi.Response('', ReadTeamSerializer(many=True))})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: openapi.Response('', ReadTeamSerializer())})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class GamesList(generics.ListCreateAPIView):
    model = Games
    serializer_class = GamesSerializer

    def get_queryset(self):
        queryset = Games.objects.all()
        season = self.request.query_params.get('season')
        host_city = self.request.query_params.get('host_city')
        year = self.request.query_params.get('year')

        if season:
            queryset = queryset.filter(season=season)
        if host_city:
            queryset = queryset.filter(host_city__name__icontains=host_city)
        if year:
            queryset = queryset.filter(year=year)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('season', openapi.IN_QUERY,
                                                              description="Season's ID",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            openapi.Parameter('host_city', openapi.IN_QUERY,
                                                              description="City's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('year', openapi.IN_QUERY,
                                                              description="Year",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            ],
                         responses={status.HTTP_200_OK: openapi.Response('', ReadGamesSerializer(many=True))})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: openapi.Response('', ReadGamesSerializer())})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class AthleteList(generics.ListCreateAPIView):
    model = Athlete
    serializer_class = AthleteSerializer

    def get_queryset(self):
        queryset = Athlete.objects.all()
        name = self.request.query_params.get('name')
        sex = self.request.query_params.get('sex')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if sex:
            queryset = queryset.filter(sex=sex)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('name', openapi.IN_QUERY,
                                                              description="Athlete's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('sex', openapi.IN_QUERY,
                                                              description="Sex's ID",
                                                              type=openapi.TYPE_STRING, required=False),
                                            ],
                         responses={status.HTTP_200_OK: openapi.Response('', ReadAthleteSerializer(many=True))})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: openapi.Response('', ReadAthleteSerializer())})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class EventList(generics.ListCreateAPIView):
    model = Event
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        name = self.request.query_params.get('name')
        sport = self.request.query_params.get('sport')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if sport:
            queryset = queryset.filter(sport_id=sport)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('name', openapi.IN_QUERY,
                                                              description="Event's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('sport', openapi.IN_QUERY,
                                                              description="Sport's ID",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            ],
                         responses={status.HTTP_200_OK: openapi.Response('', ReadEventSerializer(many=True))})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: openapi.Response('', ReadEventSerializer())})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class AthleteGameList(generics.ListCreateAPIView):
    model = AthleteGame
    serializer_class = AthleteGameSerializer

    def get_queryset(self):
        queryset = AthleteGame.objects.all()
        athlete = self.request.query_params.get('athlete')
        team = self.request.query_params.get('team')
        noc = self.request.query_params.get('noc')
        game_year = self.request.query_params.get('game_year')
        game_season = self.request.query_params.get('game_season')

        if athlete:
            queryset = queryset.filter(athlete__name__icontains=athlete)
        if team:
            queryset = queryset.filter(team__name__icontains=team)
        if noc:
            queryset = queryset.filter(team__noc__pk=noc)
        if game_year:
            queryset = queryset.filter(game__year=game_year)
        if game_season:
            queryset = queryset.filter(game__season=game_season)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('athlete', openapi.IN_QUERY,
                                                              description="Athlete's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('team', openapi.IN_QUERY,
                                                              description="Team's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('noc', openapi.IN_QUERY,
                                                              description="NOC three-letter code",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('game_year', openapi.IN_QUERY,
                                                              description="Games's year",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            openapi.Parameter('game_season', openapi.IN_QUERY,
                                                              description="Games's season ID",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            ],
                         responses={status.HTTP_200_OK: openapi.Response('', ReadAthleteGameSerializer(many=True))})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class AthleteGameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AthleteGame.objects.all()
    serializer_class = AthleteGameSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: openapi.Response('', ReadAthleteGameSerializer())})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class AthleteGameEventList(generics.ListCreateAPIView):
    model = AthleteGameEvent
    serializer_class = AthleteGameEventSerializer

    def get_queryset(self):
        queryset = AthleteGameEvent.objects.all()
        athlete = self.request.query_params.get('athlete')
        team = self.request.query_params.get('team')
        noc = self.request.query_params.get('noc')
        game_year = self.request.query_params.get('game_year')
        game_season = self.request.query_params.get('game_season')
        event = self.request.query_params.get('event')
        sport = self.request.query_params.get('sport')
        has_medal = self.request.query_params.get('has_medal')
        medal = self.request.query_params.get('medal')

        if athlete:
            queryset = queryset.filter(athlete_game__athlete__name__icontains=athlete)
        if team:
            queryset = queryset.filter(athlete_game__team__name__icontains=team)
        if noc:
            queryset = queryset.filter(athlete_game__team__noc__pk=noc)
        if game_year:
            queryset = queryset.filter(athlete_game__game__year=game_year)
        if game_season:
            queryset = queryset.filter(athlete_game__game__season=game_season)
        if event:
            queryset = queryset.filter(event__pk=event)
        if sport:
            queryset = queryset.filter(event__sport__pk=sport)
        if has_medal:
            if has_medal == 'true':
                queryset = queryset.filter(medal__isnull=False)
            if has_medal == 'false':
                queryset = queryset.filter(medal__isnull=True)
        if medal:
            queryset = queryset.filter(medal=medal)

        return queryset

    @swagger_auto_schema(manual_parameters=[openapi.Parameter('athlete', openapi.IN_QUERY,
                                                              description="Athlete's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('team', openapi.IN_QUERY,
                                                              description="Team's name",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('noc', openapi.IN_QUERY,
                                                              description="NOC three-letter code",
                                                              type=openapi.TYPE_STRING, required=False),
                                            openapi.Parameter('game_year', openapi.IN_QUERY,
                                                              description="Games's year",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            openapi.Parameter('game_season', openapi.IN_QUERY,
                                                              description="Games's season ID",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            openapi.Parameter('event', openapi.IN_QUERY,
                                                              description="Event's ID",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            openapi.Parameter('sport', openapi.IN_QUERY,
                                                              description="Sport's ID",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            openapi.Parameter('has_medal', openapi.IN_QUERY,
                                                              description="If has medal or not",
                                                              type=openapi.TYPE_BOOLEAN, required=False),
                                            openapi.Parameter('medal', openapi.IN_QUERY,
                                                              description="Medal's ID",
                                                              type=openapi.TYPE_INTEGER, required=False),
                                            ],
                         responses={status.HTTP_200_OK: openapi.Response('',
                                                                         ReadAthleteGameEventSerializer(many=True))})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class AthleteGameEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AthleteGameEvent.objects.all()
    serializer_class = AthleteGameEventSerializer

    @swagger_auto_schema(responses={status.HTTP_200_OK: openapi.Response('', ReadAthleteGameEventSerializer())})
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)
