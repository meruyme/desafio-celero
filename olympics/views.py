from django.shortcuts import render
from rest_framework import generics

from olympics.models import City, Sport, Team
from olympics.serializers import CitySerializer, SportSerializer, TeamSerializer, ReadTeamSerializer


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
