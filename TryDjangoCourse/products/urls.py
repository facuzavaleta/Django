from django.contrib import admin
from django.urls import include, path

from pages.views import home_view, contact_view, about_view, social_view
from products.views import (
    product_detail_view, 
    product_create_view, 
    product_delete_view,
    product_list_view, 
    dynamic_lookup_view,
    product_update_view)

app_name = 'products'
urlpatterns = [
    path('', product_list_view),
    path('create/', product_create_view),
    path('<int:id>/', dynamic_lookup_view, name="product-detail"),
    path('<int:id>/delete/', product_delete_view),
    path('<int:id>/update/', product_update_view),
]