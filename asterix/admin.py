from django.contrib import admin
from .models import Role, Creator, Media, MediaTitle, Character, Alias,Location, Faction
# Register your models here.

admin.site.register(Role)
admin.site.register(Creator)
admin.site.register(Media)
admin.site.register(MediaTitle)
admin.site.register(Character)
admin.site.register(Alias)
admin.site.register(Location)
admin.site.register(Faction)