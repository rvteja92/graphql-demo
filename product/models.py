from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=256)
    mrp = models.DecimalField(verbose_name='M.R.P.', max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=256)

    related_products = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.title
    