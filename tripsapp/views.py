from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated
from .models import Trips
from .serializers import CustomTokenObtainPairSerializer, UserCreateSerializer, UsersListSerializer, UpdateTripsSerializer, CreateTripsSerializer, TripsListSerializer
from .permissions import IsOwner


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer



class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer

class TripsListAPIView(ListAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsListSerializer


class CreateView(CreateAPIView):
    serializer_class = CreateTripsSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(DestroyAPIView):
    queryset = Trips.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


#As a user, I can update a trip

class UpdateView(UpdateAPIView):
    queryset = Trips.objects.all()
    serializer_class = UpdateTripsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsOwner]