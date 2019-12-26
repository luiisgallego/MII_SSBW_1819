from django.urls import path
from . import views
from django.conf.urls import include, url
from rest_framework import routers
from .viewsets import PelisViewSet

router = routers.DefaultRouter()
router.register('pelis', PelisViewSet, 'peli')

urlpatterns = [
	path('hello_world', views.hola_mundo),
    path('tarea5/', views.main_mongoengine),
    path('tarea5/all', views.consultas_mongoengine),
    path('tarea5/one/<id>', views.consultas_mongoengine_2),
    path('tarea7', views.allPelis, name="tarea7"),
    path('tarea7/createPeli', views.createPeli, name="create"),
    path('tarea7/updatePeli/<id>', views.updatePeli, name="update"),
    path('tarea7/deletePeli/<id>', views.deletePeli, name="delete"),
    path('like', views.like, name="like"),
    path('dislike', views.dislike, name="dislike"),
    path('api_pelis',    views.api_pelis),  # GET lista todas, POST añade
    path('api_peli/<id>', views.api_peli),  # GET lista una,   PUT modifica, DELETE borrra
    url('api', include(router.urls)),       # Incluye todo el API CRUD
]
