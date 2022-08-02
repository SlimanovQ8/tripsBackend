from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django import forms



from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Trips
from .serializers import CustomTokenObtainPairSerializer, UserCreateSerializer, UsersList, UpdateTripsSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersList

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