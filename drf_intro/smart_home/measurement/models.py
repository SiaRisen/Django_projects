from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['name']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', db_column='sensor')
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Температура в момент измерения')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата измерения')
    image = models.ImageField(null=True, upload_to='measurement/static/images',
                              height_field=None,
                              width_field=None,
                              max_length=10000, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-updated_at']
