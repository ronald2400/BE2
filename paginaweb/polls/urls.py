from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('paginabaldurs/', views.paginabaldurs, name='paginabaldurs'),
    path('paginabanco/', views.paginabanco, name='paginabanco'),
    path('registrar/', views.registrar, name='registrar'),
    path('ingresar/', views.ingresar, name='ingresar'),
]