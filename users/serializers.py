from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import serializers

admin.autodiscover()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")
