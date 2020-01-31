from django.contrib import admin

from product.models import Product
from review.models import Review


admin.site.register(Product)
admin.site.register(Review)
