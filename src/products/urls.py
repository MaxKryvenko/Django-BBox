from django.urls import path
from .views import product_detail_view, product_create_view, product_list_view

from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'

urlpatterns = [
    path('<int:id>/', product_detail_view, name='product_detail'),
    path('create/', product_create_view, name='product_create'),
    path('list/', product_list_view, name='product_list'),
] 