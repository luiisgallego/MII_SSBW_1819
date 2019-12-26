from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from urllib.request import urlopen
from .models import Pelis
from .forms import PelisForm
from django.http import JsonResponse
import logging
import json
from django.contrib.auth.decorators import login_required
from .serializers import PelisSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

# Obtener el logger
logger = logging.getLogger(__name__)


def hola_mundo(request):
    salida = '''<html>Hola mundo</html>'''
    return HttpResponse(salida)

# ------------ TAREA 5 ------------------ #

# Inicialmente entramos en el formulario
def main_mongoengine(request): return render(request, 'pelis/formulario.html')


def modificaPoster(result):
    for obj in result:
        print("-----> ",obj.poster)

        # NoneType no es iterable
        if obj.poster is not None:
            if 'https' in obj.poster: pass
            else :
                poster = obj.poster
                poster = poster.replace("http", "https")
                obj.poster = poster
                obj.save()


# Procesamos la info del formulario
def consultas_mongoengine(request):

    pelicula = request.POST.get('pelicula')
    anio = request.POST.get('anio')
    actor = request.POST.get('actor')

    if pelicula != "" and anio != "" and actor != "":
        # peli = Pelis.objects().get(title=pelicula)

        # Tenemos comprobar que vamos a tener resultados, sino devuelve error django
        if Pelis.objects().filter(title=pelicula, year=anio, actors=actor).count() > 0:
            result = Pelis.objects(title=pelicula, year=anio, actors=actor)            
            modificaPoster(result)
            context = { 'pelis' : result, 'all': "True" }
            return render(request, 'pelis/info_peliculas.html', context)
        else: 
            # Volvemos al formulario si no tenemos resultados
            return render(request, 'pelis/formulario.html')

    elif pelicula != "" and anio != "":
        if Pelis.objects().filter(title=pelicula, year=anio).count() > 0:
            result = Pelis.objects(title=pelicula, year=anio)            
            modificaPoster(result)
            context = { 'pelis' : result, 'all': "True" }
            return render(request, 'pelis/info_peliculas.html', context)
        else: return render(request, 'pelis/formulario.html')

    elif pelicula != "" and actor != "":
        if Pelis.objects().filter(title=pelicula, actors=actor).count() > 0:
            result = Pelis.objects(title=pelicula, actors=actor)            
            modificaPoster(result)
            context = { 'pelis' : result, 'all': "True" }
            return render(request, 'pelis/info_peliculas.html', context)
        else: return render(request, 'pelis/formulario.html')

    elif anio != "" and actor != "":
        if Pelis.objects().filter(year=anio, actors=actor).count() > 0:
            result = Pelis.objects(year=anio, actors=actor)            
            modificaPoster(result)
            context = { 'pelis' : result, 'all': "True" }
            return render(request, 'pelis/info_peliculas.html', context)
        else: return render(request, 'pelis/formulario.html')

    elif pelicula != "":
        if Pelis.objects().filter(title=pelicula).count() > 0:
            result = Pelis.objects(title=pelicula)            
            modificaPoster(result)       
            context = { 'pelis' : result, 'all': "True" }
            return render(request, 'pelis/info_peliculas.html', context)
        else: return render(request, 'pelis/formulario.html')

    elif anio != "":
        if Pelis.objects().filter(year=anio).count() > 0:
            result = Pelis.objects(year=anio)            
            modificaPoster(result)
            context = { 'pelis' : result, 'all': "True" }
            return render(request, 'pelis/info_peliculas.html', context)
        else: return render(request, 'pelis/formulario.html')

    elif actor != "":
        if Pelis.objects().filter(actors__contains=actor).count() > 0:
            result = Pelis.objects(actors__contains=actor)            
            modificaPoster(result)
            context = { 'pelis' : result, 'all': "True" }
            return render(request, 'pelis/info_peliculas.html', context)
        else: return render(request, 'pelis/formulario.html')

    else:
        return render(request, 'pelis/formulario.html')

def consultas_mongoengine_2(request, id):
    result = Pelis.objects().get(id=id)
    context = { 'peli' : result, 'all': "False" }
    return render(request, 'pelis/info_peliculas.html', context)


# ------------ TAREA 7 ------------------ #

def allPelis(request): 
    #x = request.GET.get('actor', None) # Si no no funciona
    context = { 'pelis' : Pelis.objects }
    return render(request, 'pelis/allPelis.html', context)

@login_required
def createPeli(request):
    if(request.method == "POST"):
        form = PelisForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('tarea7'))
    else:
        form = PelisForm()
        context = { "form": form}
        return(render(request,"pelis/formPelis.html",context))

@login_required
def updatePeli(request, id):
    pelicula = Pelis.objects.get(id=id)

    if(request.method == "POST"):
        form = PelisForm(request.POST,instance=pelicula)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('tarea7'))
    else:    
        form = PelisForm(instance=pelicula)
        context = { "form": form}
        return(render(request,"pelis/formPelis.html",context))

@login_required
def deletePeli(request,id):
    pelicula = Pelis.objects.get(id=id)
    pelicula.delete()
    return HttpResponseRedirect(reverse('tarea7'))

# ------------ TAREA 11 ------------------ #

def like(request):
    id = request.POST['id']
    peli = Pelis.objects.get(id=id)

    if peli.likes is not None:
        peli.likes = peli.likes + 1
        peli.save()
        return JsonResponse('OK')
    else:
        peli.likes = 1
        peli.save()
        return JsonResponse('OK')

def dislike(request):
    id = request.POST['id']
    peli = Pelis.objects.get(id=id)

    if peli.likes is not None:
        peli.likes = peli.likes - 1
        peli.save()
        return JsonResponse('OK')
    else:
        peli.likes = 0
        peli.save()
        return JsonResponse('OK')


# ------------ TAREA 12 ------------------ #

@csrf_exempt
def api_pelis(request):
	if request.method == 'GET':
		pelis = Pelis.objects.all()[:10]
		serializer = PelisSerializer(pelis, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PelisSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)

	logger.debug('Error')
	return JsonResponse(serializers.errors, stauts=400)


@csrf_exempt
def api_peli(request,id):
    try: peli = Pelis.objects().get(id=id)
    except: 
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PelisSerializer(peli)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        datos = JSONParser().parse(request)
        serializer = PelisSerializer(peli, data=datos)
        if serializer.is_valid():
            serializer.save()
            return(JsonResponse(serializer.data,status=200))
        return JsonResponse(serializer.errors, status=400)

    if request.method == "DELETE":
        peli.delete()
        return(HttpResponse(status=204))
    
