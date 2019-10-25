from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=1000000)
    stock = models.BigIntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    discount = models.FloatField


