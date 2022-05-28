from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
