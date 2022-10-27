from django.db import models

class Shop (models.Model):
    Sname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    address = models.TextField(max_length=100)

class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=20)
    shop = models.ForeignKey(Shop,
                            null=True,
                            blank=True,
                            related_name="item_product",
                            on_delete=models.SET_NULL)