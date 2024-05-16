from django.urls import path
from .views import index, cart, to_cart, product_by_category, detail

urlpatterns = [
    path('', index, name="index"),
    path('cart/', cart, name="cart"),
    path('to-cart/<int:product_id>/<str:action>/', to_cart, name="to_cart"),
    path('by-category/<int:category_pk>/', product_by_category, name="by_category"),
    path('detail/<int:product_id>/', detail, name="detail")
]
