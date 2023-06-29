from rest_framework import serializers

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'updated_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
