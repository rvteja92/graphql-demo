from django import forms
from django.shortcuts import get_object_or_404

import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation, Field
from graphene_django.rest_framework.mutation import SerializerMutation

from .models import Review


class UpdateReviewMutation(graphene.Mutation):
    id = graphene.Int()
    rating = graphene.Int()
    review = graphene.String()
    user_name = graphene.String()

    class Arguments:
        id = graphene.Int()
        rating = graphene.Int()
        review = graphene.String()

    def mutate(self, info, rating, review, id):
        review_obj = get_object_or_404(Review, pk=id)
        review_obj.rating = rating
        review_obj.review = review
        review_obj.save()

        return UpdateReviewMutation(
            id=review_obj.id,
            rating=review_obj.rating,
            review=review_obj.review,
            user_name=review_obj.user_name
        )
