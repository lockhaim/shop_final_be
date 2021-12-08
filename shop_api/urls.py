from django.urls import path
from . import views

urlpatterns = [
    path('api/products', views.ProductList.as_view(), name='product_list'), # api/products will be routed to the productList view for handling
    # path('api/products/<int:pk>', views.ProductList.as_view(), name='product_list'),
    path('api/products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'), # api/products will be routed to the ContactDetail view for handling
]
