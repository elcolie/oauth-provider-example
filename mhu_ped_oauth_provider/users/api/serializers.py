from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
