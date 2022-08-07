from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from tripsapp.models import Trips, UserProfile


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password"]

    def create(self, validated_data):
        firstname = validated_data["first_name"]
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]

        new_user = User(first_name=firstname, email= email, username= username,)
        new_user.set_password(password)
        new_user.save()
        newProfile = UserProfile(user=new_user, id= new_user.id)
        newProfile.save()

        return validated_data



class ViewTripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ["id", "title", "description", "image"]


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UsersProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'image']

    def check_user(self, obj):
        if obj.owner != self.context["request"].user:
            raise serializers.ValidationError("You are not the owner of this profile")

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['email'] = user.email
        token['user_id'] = user.id
        return token

class TripsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = "__all__"

class GetUserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
class CreateTripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ["title", "description", "image"]
        extra_kwargs = {
            "owner": {
                "read_only": True
            }
        }
    def create(self, validated_data):
        title = validated_data["title"]
        description = validated_data["description"]
        image = validated_data["image"]
        #id = validated_data["id"]
        owner = self.context["request"].user
        print(owner)
        new_trip = Trips(title=title, description=description, image=image, user=owner)
        new_trip.save()
        return validated_data


class UpdateTripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ['title', 'description','image']

    def check_user(self, obj):
        if obj.owner != self.context["request"].user:
            raise serializers.ValidationError("You are not the owner of this trip")