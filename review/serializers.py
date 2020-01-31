from rest_framework import serializers

from .models import Review


class ReviewSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['product']
