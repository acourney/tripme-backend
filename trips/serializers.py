from rest_framework import serializers
from .models import Trip, Todo
from djoser.serializers import UserCreateSerializer, UserSerializer
from users.models import User
from django.http import JsonResponse

class MemberSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):

    def to_representation(self, value):
        # members = User.objects.all().values('id', 'email', 'username')
        # members_list = list(members)
        # return f'{value.id}, {value.username}'
        return value.id

    class Meta:
        model = 'users.User'
        fields = ('id', 'email', 'username')


class TripSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='todo_detail')

    trip_url = serializers.ModelSerializer.serializer_url_field(
        view_name='trip_detail')

    owner = serializers.ReadOnlyField(source='owner.username')

    members = MemberSerializer(many=True, queryset=User.objects.all())



    class Meta:
        model = Trip
        fields = ('id', 'label', 'destination', 'todos', 'trip_url', 'owner', 'photo', 'members')
        # depth = 1
    
    # def update(self, data):




class TodoSerializer(serializers.HyperlinkedModelSerializer):
    trip = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='trip_detail')

    trip_id = serializers.PrimaryKeyRelatedField(
        source='trip', queryset=Trip.objects.all())

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('id', 'summary', 'body', 'trip', 'trip_id', 'owner', )
            

# class TripMemberSerializer(serializers.HyperlinkedModelSerializer):
#     trip = serializers.HyperlinkedRelatedField(
#         read_only=True, view_name='trip_detail')

#     members = serializers.HyperlinkedRelatedField(
#         read_only=True, many=True, view_name='users_detail')

#     trip_id = serializers.PrimaryKeyRelatedField(
#         source='trip', queryset=Trip.objects.all())

#     members = serializers.HyperlinkedRelatedField(
#         read_only=True, view_name='member_detail')

#     class Meta:
#         model = Trip
#         fields = ('id', 'members', 'trip', 'trip_id',)