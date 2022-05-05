from rest_framework import serializers

from olympics.models import Athlete, City, Sport, Noc, Event, Games, Team


class NocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noc
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class ReadEventSerializer(serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        return super(EventSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        return ReadEventSerializer(instance).data

    class Meta:
        model = Event
        fields = '__all__'


class ReadGamesSerializer(serializers.ModelSerializer):
    host_city = CitySerializer()

    class Meta:
        model = Games
        fields = '__all__'


class GamesSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        return super(GamesSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        return ReadGamesSerializer(instance).data

    class Meta:
        model = Games
        fields = '__all__'


class ReadTeamSerializer(serializers.ModelSerializer):
    noc = NocSerializer()

    class Meta:
        model = Team
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        return super(TeamSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        return ReadTeamSerializer(instance).data

    class Meta:
        model = Team
        fields = '__all__'
