from django.urls import path
from .views import EndpointListView, EndpointDetailView

app_name = 'endpoints'

urlpatterns = [
    path('', EndpointListView.as_view(), name='endpoint_list'),
    path('list/', EndpointListView.as_view(), name='endpoint_list'),
    path('<str:sku>/', EndpointDetailView.as_view(), name='endpoint_detail'),

]