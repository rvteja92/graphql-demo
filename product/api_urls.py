from django.urls import path

from .views import (
    ProductList, ProductDetailsV1, ProductReviewsV1, ProductDetailsV2, ProductDetailsV3,
    ProductDetailsV4, ProductDetailsV5
)

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/v1/', ProductDetailsV1.as_view(), name='product_details_v1'),
    path('<int:pk>/v2/', ProductDetailsV2.as_view(), name='product_details_v2'),
    path('<int:product_id>/reviews/v2/', ProductReviewsV1.as_view(), name='product_reviews_v2'),
    path('<int:pk>/v3/', ProductDetailsV3.as_view(), name='product_details_v3'),
    path('<int:pk>/v4/', ProductDetailsV4.as_view(), name='product_details_v4'),
    path('<int:pk>/v5/', ProductDetailsV5.as_view(), name='product_details_v5'),
]