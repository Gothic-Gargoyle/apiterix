from rest_framework import serializers
from .models import Creator, Media, MediaTitle, Character, Alias, Location, Faction, Role

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    roles = RoleSerializer(many=True)  # Nested serializer

    class Meta:
        model = Creator
        fields = '__all__'

class MediaSerializer(serializers.HyperlinkedModelSerializer):
    writers = CreatorSerializer(many=True, read_only=True)
    illustrators = CreatorSerializer(many=True, read_only=True)
    directors = CreatorSerializer(many=True, read_only=True)
    developers = CreatorSerializer(many=True, read_only=True)

    class Meta:
        model = Media
        fields = '__all__'

class MediaTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MediaTitle
        fields = '__all__'

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = '__all__'

class AliasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alias
        fields = '__all__'

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = '__all__'
