from rest_framework import serializers
from .models import UserGroup


class UserGroupSerializer(serializers.Serializer):
    users = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='user_group_detail')
