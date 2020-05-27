import graphene
import time

from graphene_django.types import DjangoObjectType

from product.models import Product
from review.models import Review


class ProductType(DjangoObjectType):
    delayed_field = graphene.String()

    def resolve_delayed_field(self, info):
        time.sleep(4)
        return 'delayed text'

    class Meta:
        model = Product


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class Query(object):
    all_products = graphene.List(
        ProductType,
        pagesize=graphene.Int(),
        offset=graphene.Int(),
    )
    all_reviews = graphene.List(
        ReviewType,
        pagesize=graphene.Int(),
        offset=graphene.Int(),
    )

    product = graphene.Field(ProductType, id=graphene.Int())
    review = graphene.Field(ReviewType, id=graphene.Int())

    def resolve_all_products(self, info, pagesize=None, offset=0, **kwargs):
        query_set = Product.objects.all()

        if pagesize is not None:
            return query_set[offset: offset + pagesize]

        return query_set

    def resolve_all_reviews(self, info,pagesize=None, offset=0, **kwargs):
        query_set = Review.objects.select_related('product').all()

        if pagesize is not None:
            return query_set[offset: offset + pagesize]

        return query_set

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
