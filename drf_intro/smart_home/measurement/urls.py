from django.urls import path

from .views import SensorDetailView, SensorsListView, MeasurementsListView

urlpatterns = [
    path('sensors/', SensorsListView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsListView.as_view()),
]
