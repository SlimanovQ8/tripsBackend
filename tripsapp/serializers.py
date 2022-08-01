from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from tripsapp.models import Trips


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password"]

    def create(self, validated_data):
        firstname = validated_data["first_name"]
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]
        new_user = User(first_name=firstname, email= email, username= username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class ViewTripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ["id", "title", "description", "image"]
        