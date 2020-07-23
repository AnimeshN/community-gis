from django.urls import path
from . import views
urlpatterns = [
    path("", views.apiOverview, name='api_overview'),
    path("hospital_list/", views.HospitalList, name='hospital_list'),
    path("hospital_details/<str:pk>/",
         views.HospitalDetails, name='hospital_details'),
    path("hospital_add/",
         views.HospitalAdd, name='hospital_add'),
    path("hospital_update/<str:pk>/",
         views.HospitalUpdate, name='hospital_update'),
    path("hospital_delete/<str:pk>/",
         views.HospitalDelete, name='hospital_delete'),
]
