from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portal-home'),
    path('novedades', views.novedades, name='portal-novedades'),
]
