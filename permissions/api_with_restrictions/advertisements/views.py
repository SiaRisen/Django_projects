from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement, Favorite
from advertisements.permissions import IsOwnerForFavorite, IsOwnerOrAdmin
from advertisements.serializers import AdvertisementSerializer, FavoriteSerializer
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create"]:
            permissions = [IsAuthenticatedOrReadOnly()]
        elif self.action in ["update", "partial_update", "destroy"]:
            permissions = [IsAuthenticated(), IsOwnerOrAdmin()]
        else:
            permissions = []
        return [permission() for permission in permissions]


class FavoriteViewSet(ModelViewSet):
    """ViewSet для избранного."""

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_permissions(self):
        """Получение прав для действий."""

        return [IsAuthenticated(), IsOwnerForFavorite()]

    def get_queryset(self):
        """Получение избранного определенного пользователя."""

        return Favorite.objects.all().filter(user=self.request.user)
