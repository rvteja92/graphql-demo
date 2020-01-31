from django.urls import reverse

from rest_framework import serializers

from .models import Product

from review.serializers import ReviewSerializerV1


class ProductSerializerV1(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'mrp', 'price', 'description']


class ProductSerializerV2(serializers.ModelSerializer):

    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'mrp', 'price', 'description', 'reviews']

    def get_reviews(self, object):
        return reverse('product_reviews_v2', kwargs={'product_id': object.id})


class ProductSerializerV3(serializers.ModelSerializer):

    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'mrp', 'price', 'description', 'reviews']

    def get_reviews(self, object):
        return ReviewSerializerV1(object.review_set.all(), many=True).data


class ProductSerializerV4(serializers.ModelSerializer):
    
    reviews = serializers.SerializerMethodField()
    related_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product_details_v4'
    )

    class Meta:
        model = Product
        fields = ['title', 'mrp', 'price', 'description', 'related_products',
            'reviews']

    def get_reviews(self, object):
        return ReviewSerializerV1(object.review_set.all(), many=True).data


class ProductSerializerV5(serializers.ModelSerializer):
    
    reviews = serializers.SerializerMethodField()
    related_products = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'mrp', 'price', 'description', 'related_products',
            'reviews']

    def get_reviews(self, object):
        return ReviewSerializerV1(object.review_set.all(), many=True).data

    def get_related_products(self, object):
        return ProductSerializerV4(object.related_products.all(), many=True, context={'request': self.context['request']}).data