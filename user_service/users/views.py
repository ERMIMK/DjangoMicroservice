from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the User Service!")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
