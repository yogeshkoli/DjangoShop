
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<slug:category_slug>/', views.product, name='products_by_category')
]
