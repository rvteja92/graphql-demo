from django.db import models

from django.core.validators import MaxValueValidator

from product.models import Product


class Review(models.Model):
    user_name = models.CharField(max_length=30)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = models.CharField(max_length=256)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.review[:20]
