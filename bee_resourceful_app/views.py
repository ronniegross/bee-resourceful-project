from django.shortcuts import render

from rest_framework import viewsets

from .serializers import UserSerializer, ResourceSerializer
from .models import User, Resource


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ResourceView(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer