from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
