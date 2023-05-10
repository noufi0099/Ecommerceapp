from django.urls import path
from eapp import views

urlpatterns=[
    path('customers/',views.CustomerListCreateView.as_view()),
    path('customers/<int:pk>', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('customers/<int:pk>/update', views.CustomerRetrieveUpdateDeleteView.as_view(), name='customer-update'),

    path('customers/<int:customer_pk>/products/<int:pk>/', views.ProductRetrieveUpdateDeleteView.as_view(), name='product-retrieve-update-delete'),
    
]