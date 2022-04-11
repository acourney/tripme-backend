from rest_framework import serializers
from .models import Trip, Todo


class TripSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='todo_detail')

    trip_url = serializers.ModelSerializer.serializer_url_field(
        view_name='trip_detail')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Trip
        fields = ('id', 'label', 'destination', 'todos', 'trip_url', 'owner', 'photo')


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    trip = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='trip_detail')

    trip_id = serializers.PrimaryKeyRelatedField(
        source='trip', queryset=Trip.objects.all())

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('id', 'summary', 'body', 'trip', 'trip_id', 'owner', )
            