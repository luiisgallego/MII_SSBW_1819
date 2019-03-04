from django.urls import path
from . import views

urlpatterns = [
	# path('hola_mundo', views.hola_mundo),	# entrada str
    path('1/<str:usuario>', views.ejercicio_1),	# entrada str
]
