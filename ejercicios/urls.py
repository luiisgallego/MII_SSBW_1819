from django.urls import path
from . import views

urlpatterns = [
	path('0_1', views.hola_mundo),	
    path('0_2/<usuario>', views.hola_mundo_nombre),	
	path('1/<lista>', views.ejercicio1),
	path('2/<lista>', views.ejercicio2),
	path('3/<entrada>', views.ejercicio3),
	path('4/<entrada>', views.ejercicio4),
	path('9', views.expresiones_regulares),
	path('10', views.consultas_pymongo),
]
