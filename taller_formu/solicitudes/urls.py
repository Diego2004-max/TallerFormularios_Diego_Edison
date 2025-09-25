from django.urls import path
from . import views

urlpatterns = [
    path('nueva/', views.solicitud_create, name='solicitud_create'),
    path('exito/', views.solicitud_success, name='solicitud_success'),
]
