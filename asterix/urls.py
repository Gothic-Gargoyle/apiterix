from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreatorViewSet, MediaViewSet, MediaTitleViewSet, CharacterViewSet, AliasViewSet, LocationViewSet, FactionViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'creators', CreatorViewSet)
router.register(r'media', MediaViewSet)
router.register(r'media-titles', MediaTitleViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'aliases', AliasViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'factions', FactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]