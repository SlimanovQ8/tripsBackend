from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated
from .models import Trips, UserProfile
from .serializers import UpdateProfileSerializer, UsersProfileListSerializer, CustomTokenObtainPairSerializer, UserCreateSerializer, UsersListSerializer, UpdateTripsSerializer, CreateTripsSerializer, TripsListSerializer, GetUserProfile
from .permissions import IsOwner


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer

class UsersProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UsersProfileListSerializer

class UserProfileAPIView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class =  GetUserProfile
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class ProfileUpdateView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UpdateProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsOwner]


class TripsListAPIView(ListAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsListSerializer

class UsersTripsListAPIView(ListAPIView):
    serializer_class = TripsListSerializer

    def get_queryset(self):
        userID = self.kwargs['object_id']
        queryset = Trips.objects.filter(user=userID)

        return queryset

class getProfile(ListAPIView):
    serializer_class = UsersProfileListSerializer

    def get_queryset(self):
        userID = self.kwargs['object_id']
        queryset = UserProfile.objects.filter(user=userID)

        return queryset

class CreateView(CreateAPIView):
    serializer_class = CreateTripsSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(DestroyAPIView):
    queryset = Trips.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsOwner]


#As a user, I can update a trip

class UpdateView(UpdateAPIView):
    queryset = Trips.objects.all()
    serializer_class = UpdateTripsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsOwner]