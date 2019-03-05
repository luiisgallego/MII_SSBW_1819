from django.urls import path
from . import views

urlpatterns = [
	path('0_1', views.hola_mundo),	
    path('0_2/<str:usuario>', views.hola_mundo_nombre),	
	path('1', views.ejercicio1),
	path('9', views.expresiones_regulares),
]
