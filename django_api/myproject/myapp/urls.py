from djagno.urls import path
from myapp.views import ProductList, ProductDetail



urlpatterns [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail')
    
    
]