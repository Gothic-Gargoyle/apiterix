from django.db import models


class TimeStampedModel(models.Model):
    """Abstract base class that adds created_at and updated_at fields to models."""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


"""
Model for roles
"""


class Role(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


"""
Model for creators
"""


class Creator(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    roles = models.ManyToManyField(Role, related_name="creators")
    media = models.ManyToManyField('Media', related_name="creators")

    def __str__(self):
        return self.name


"""
Model for Media types

"""


class MediaType(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


"""
Model for media
"""


class Media(TimeStampedModel):
    title = models.CharField(max_length=255, unique=True, help_text="Original title")
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    writers = models.ManyToManyField(Creator, related_name="written_media", blank=True)
    illustrators = models.ManyToManyField(Creator, related_name="illustrated_media", blank=True)
    directors = models.ManyToManyField(Creator, related_name="directed_media", blank=True)
    characters = models.ManyToManyField('Character', blank=True, related_name="appears_in")
    locations = models.ManyToManyField('Location', blank=True, related_name="featured_locations")
    factions = models.ManyToManyField('Faction', blank=True, related_name="featured_factions")
    first_published = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.media_type})"


"""
Model for media titles
"""


class MediaTitle(TimeStampedModel):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    translated_title = models.CharField(max_length=255, help_text="Translated title")
    language = models.CharField(max_length=2, help_text="ISO 639-1 language code")

    class Meta:
        unique_together = ('media', 'language')

    def __str__(self):
        return f"{self.translated_title} ({self.language})"


"""
Model for Characters
"""


class Character(TimeStampedModel):
    name = models.CharField(max_length=100)
    media = models.ManyToManyField(Media, related_name="featured_characters")
    first_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="first_appeared_in")
    last_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="last_appeared_in")
    hair_color = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')])
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    faction = models.ForeignKey('Faction', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Alias(TimeStampedModel):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="aliases")
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=2, help_text="ISO 639-1 language code")

    class Meta:
        unique_together = ('character', 'language')

    def __str__(self):
        return f"{self.name} ({self.language})"


"""
Model for locations
"""


class Location(TimeStampedModel):
    name = models.CharField(max_length=100)
    media = models.ManyToManyField(Media)
    faction = models.ForeignKey('Faction', on_delete=models.SET_NULL, null=True)
    first_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="first_appearance")
    last_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="last_appearance")

    def __str__(self):
        return self.name


"""
Model for Factions
"""


class Faction(TimeStampedModel):
    name = models.CharField(max_length=100)
    allies = models.ManyToManyField('self', blank=True, related_name='faction_allies', symmetrical=False)
    rivals = models.ManyToManyField('self', blank=True, related_name='faction_rivals', symmetrical=False)

    def __str__(self):
        return self.name
