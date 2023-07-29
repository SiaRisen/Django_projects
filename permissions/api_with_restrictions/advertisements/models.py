from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    DRAFT = 'DRAFT', "Черновик"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.OPEN
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
    

class Favorite(models.Model):
    """Избранное."""

    advertisement = models.ForeignKey(Advertisement, related_name='favorites', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
