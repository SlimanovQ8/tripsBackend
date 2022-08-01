from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User


from .serializers import UserCreateSerializer, ListSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListSerializer