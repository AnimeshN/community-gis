from django.urls import path
from . import views

urlpatterns = [
    path('map', views.fgis_map, name='map')
]