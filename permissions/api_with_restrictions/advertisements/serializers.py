from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Advertisement, Favorite


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at')

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        queryset = Advertisement.objects.filter(creator=self.context["request"].user, status="OPEN").count()

        if self.context["request"].method == "POST":
            if queryset > 10:
                raise ValidationError("Недопустимое количество открытых объявлений!")

        if self.context["request"].method == 'PATCH':
            if data.get("status") == 'OPEN' and queryset > 10:
                raise ValidationError("Недопустимое количество открытых объявлений!")

        return data


class FavoriteSerializer(serializers.ModelSerializer):
    """Serializer для избранного."""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ('favorite', 'advertisement', 'user')

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["user"] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании."""

        queryset = Favorite.objects.all().filter(user=self.context["request"].user,
                                                 advertisement=data['advertisement'].id)
        if queryset:
            raise ValidationError('Уже добавлено в избранное.')

        if data['advertisement'].creator == self.context["request"].user:
            raise ValidationError('Вы являетесь создателем объявления.')

        return data
