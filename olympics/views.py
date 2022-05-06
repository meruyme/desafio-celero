from django.shortcuts import render
from rest_framework import generics

from olympics.models import City, Sport, Team, Games, Athlete, Event
from olympics.serializers import CitySerializer, SportSerializer, TeamSerializer, ReadTeamSerializer, GamesSerializer, \
    AthleteSerializer, EventSerializer


class CityList(generics.ListCreateAPIView):
    model = City
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.all()
        name = self.request.query_params.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


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


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


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


class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


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


class AthleteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer


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
            queryset = queryset.filter(sport__name__icontains=sport)

        return queryset


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
