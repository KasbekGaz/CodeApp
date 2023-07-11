from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generadorContrasena/',views.generadorContrasena, name='generadorContrasena'),
]