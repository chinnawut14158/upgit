from django.db import models

class Shop (models.Model):
    Sname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.Sname

class Product (models.Model):
    shop = models.ForeignKey(Shop,
                            null=True,
                            blank=True,
                            related_name="item_product",
                            on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    image = models.ImageField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class OrderItem (models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                blank=True,
                                related_name="item_product",
                                on_delete=models.SET_NULL)
    unti = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    