from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina1),
    path('pescados', views.pescados)
]
