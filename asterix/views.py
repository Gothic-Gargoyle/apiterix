from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Creator, Media, MediaTitle, Character, Alias, Location, Faction, Role
from .serializers import CreatorSerializer, MediaSerializer, MediaTitleSerializer, CharacterSerializer, AliasSerializer, LocationSerializer, FactionSerializer, RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CreatorViewSet(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaTitleViewSet(viewsets.ModelViewSet):
    queryset = MediaTitle.objects.all()
    serializer_class = MediaTitleSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class AliasViewSet(viewsets.ModelViewSet):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class FactionViewSet(viewsets.ModelViewSet):
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer
