from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from stocks import serializers
from .models import CustomUser, Role
from .serializers import CustomUserSerializer, RoleSerializer
from rest_framework import generics

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'pk'


class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all().order_by('name')
    serializer_class = RoleSerializer

class RoleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'pk'