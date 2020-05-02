from django.urls import path
from .views import Dashboard,TDD,Ahmadnagar,Melghat

urlpatterns = [
    # path('', Dashboard, name='dashboard'),
    path('tdd', TDD, name='tdd'),
    path('ahmadnagar', Ahmadnagar, name='ahmadnagar'),
    path('melghat', Melghat, name='melghat')
]