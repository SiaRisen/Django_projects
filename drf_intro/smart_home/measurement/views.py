from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementsSerializer, SensorDetailSerializer


class SensorsListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsListView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer
