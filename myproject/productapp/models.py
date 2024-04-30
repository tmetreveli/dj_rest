from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Name')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    inventory = models.IntegerField(verbose_name='Inventory')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Category')

    def __str__(self):
        return self.name
