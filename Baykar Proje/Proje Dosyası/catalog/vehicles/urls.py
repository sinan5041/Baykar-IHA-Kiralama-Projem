from django.urls import path
from . import views

# 127.0.0.1:8000/vehicles

urlpatterns = [
    path('', views.index, name= 'vehicles'),
    path('<int:vehicle_id>', views.detail, name= 'detail'),
    path('search', views.search, name= 'search'),
]