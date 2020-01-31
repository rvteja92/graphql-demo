from django.shortcuts import render

from rest_framework import generics

from review.models import Review
from review.serializers import ReviewSerializerV1

from .models import Product
from .serializers import (
    ProductSerializerV1, ProductSerializerV2, ProductSerializerV3,
    ProductSerializerV4, ProductSerializerV5
)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV1


class ProductDetailsV1(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV1


class ProductDetailsV2(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV2


class ProductReviewsV1(generics.ListAPIView):

    serializer_class = ReviewSerializerV1

    def get_queryset(self):
        print(self.kwargs)
        return Review.objects.filter(product__id=self.kwargs['product_id'])

    
class ProductDetailsV3(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV3


class ProductDetailsV4(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV4


class ProductDetailsV5(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerV5