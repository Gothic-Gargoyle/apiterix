from django.db import models
from simple_history.models import HistoricalRecords

"""
Model for creators
"""
class Creator(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=50, choices=[
        ('Writer', 'Writer'),
        ('Illustrator', 'Illustrator'), 
        ('Director', 'Director'), 
        ('Developer', 'Developer')])
    history = HistoricalRecords()

    def __str__(self):
        return self.name 

"""
Model for media
"""
class Media(models.Model):
    MEDIA_TYPES = [
        ('Comic', 'Comic'),
        ('Movie', 'Movie'),
        ('Game', 'Game'),
    ]
    
    title = models.CharField(max_length=255, unique=True, help_text="Original title")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)  # Specifies if it's a comic, movie, or game
    writers = models.ManyToManyField(Creator, related_name="written_media", blank=True)
    illustrators = models.ManyToManyField(Creator, related_name="illustrated_media", blank=True)
    directors = models.ManyToManyField(Creator, related_name="directed_media", blank=True)
    developers = models.ManyToManyField(Creator, related_name="developed_media", blank=True)
    characters = models.ManyToManyField('Character', blank=True)
    first_published = models.DateField()
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.title} ({self.media_type})"
    
"""
Model for media titles
"""
class MediaTitle(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    translated_title = models.CharField(max_length=255, help_text="Translated title")
    language = models.CharField(max_length=2, help_text="ISO 639-1 language code")
    history = HistoricalRecords()

    class Meta:
        unique_together = ('media', 'language')

    def __str__(self):
        return f"{self.translated_title} ({self.language})"

"""
Model for Characters
"""
class Character(models.Model):
    name = models.CharField(max_length=100)
    media = models.ManyToManyField(Media)
    first_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="first_appeared_in")
    last_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="first_appeared_in")
    hair_color = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')])
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    faction = models.ForeignKey('Faction', on_delete=models.SET_NULL, null=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.name

class Alias(models.Model):
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
class Location(models.Model):
    name = models.CharField(max_length=100)
    media = models.ManyToManyField(Media)
    faction = models.ForeignKey('Faction', on_delete=models.SET_NULL, null=True)
    first_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="first_appearance")
    last_appearance = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, related_name="last_appearance")
    history = HistoricalRecords()

    def __str__(self):
        return self.name

"""
Model for Factions
"""
class Faction(models.Model):
    name = models.CharField(max_length=100)
    history = HistoricalRecords()
    allies = models.ManyToManyField('self', blank=True, related_name='faction_allies', symmetrical=False)
    rivals = models.ManyToManyField('self', blank=True, related_name='faction_rivals', symmetrical=False)

    def __str__(self):
        return self.name