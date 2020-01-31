import graphene

from graphene_django.types import DjangoObjectType

from product.models import Product
from review.models import Review


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class Query(object):
    all_products = graphene.List(ProductType)
    all_reviews = graphene.List(ReviewType)

    product = graphene.Field(ProductType, id=graphene.Int())
    review = graphene.Field(ReviewType, id=graphene.Int())

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_all_reviews(self, info, **kwargs):
        return Review.objects.select_related('product').all()

    def resolve_product(self, info, **kwargs):
        product_id = kwargs.get('id')

        if product_id is not None:
            return Product.objects.get(id=product_id)

        return None

    def resolve_review(self, info, **kwargs):
        review_id = kwargs.get('id')

        if review_id is not None:
            return Review.objects.get(id=review_id + 5)

        return None
