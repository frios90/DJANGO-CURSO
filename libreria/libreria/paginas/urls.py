from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('libro/<int:b_id>', views.libro, name="libro")
]