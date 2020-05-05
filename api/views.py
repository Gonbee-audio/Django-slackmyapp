from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, routers
from slack.models import UserCreate
from .serializer import UserCreateSerializers

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = UserCreate.objects.all()
    serializer_class = UserCreateSerializers