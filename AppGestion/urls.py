from django.urls import path, re_path
from . import views

urlpatterns = [
    path('listar/', views.ProductoListView.as_view(), name='listar_productos'),
    path('insertar/', views.insertar_producto, name='insertar_producto'),
    path('modificar/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    # Redirección desde /producto/ a /producto/listar/
    re_path(r'^$', views.ProductoListView.as_view()),
]