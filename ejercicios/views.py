from django.shortcuts import render
from django.shortcuts import HttpResponse
from urllib.request import urlopen
from pymongo import MongoClient
import re

############### TAREA 1 ################

def hola_mundo(request):
    salida = '''<html>Hola mundo</html>'''
    return HttpResponse(salida)

def hola_mundo_nombre(request, usuario):
    salida = '''<html>Hola mundo %s</html>''' % (usuario)
    return HttpResponse(salida)

############### TAREA 2 ################

def ejercicio1(request, lista):
	lista = lista.split()
	contador = 0

	for valor in lista:
		if len(valor) > 1 and valor[0] == valor[len(valor) - 1]:
			contador += 1

	salida = '''<html>Solución: %s</html>''' % (contador)
	return HttpResponse(salida)

def ejercicio2(request, lista):
	lista = lista.split()
	anterior = lista[0]

	for i,valor in enumerate(lista[1:]):
		if anterior == valor:
			lista.pop(i)

		anterior = valor
	
	salida = '''<html>Solución: %s</html>''' % (lista)
	return HttpResponse(salida)

def ejercicio3(request, entrada):
	solucion = ""	

	if len(entrada) > 2:
		solucion += entrada[0:2] + entrada[len(entrada)-2:len(entrada)]	
	
	salida = '''<html>Solución: %s</html>''' % (solucion)
	return HttpResponse(salida)

def ejercicio4(request, entrada):
	solucion = ""
	final = entrada[len(entrada)-3:len(entrada)]	
	
	if len(entrada) > 2 and final != "ing":
		solucion = entrada + "ing"
	elif len(entrada) > 2 and final == "ing":
		solucion = entrada + "ly"
	else: solucion = entrada
	
	salida = '''<html>Solución: %s</html>''' % (solucion)
	return HttpResponse(salida)

def ejercicio5(request):
    salida = '''<html>AUN POR REALIZAR....</html>'''
    return HttpResponse(salida)


############### TAREA 3 ################

def extract_names(request):

	# Leemos la URL, transformamos y guardamos
	url = "http://ep00.epimg.net/rss/deportes/portada.xml"
	file = urlopen(url)
	data = file.read()
	file.close()
	data = data.decode('utf-8')

	# Expresiones regulares
	titulos = re.findall("<item>\W*<title><!\[CDATA\[(.+?)\]\]><\/title>", data)
	urlImagenes = re.findall(r'<enclosure url="(.+?)"', data)

	context = {
		'año': 2019,
		'titulos': titulos
	}

	return render(request, 'ejercicios/nombres.html', context)

############### TAREA 4 ################

# Conectamos con mongo
client = MongoClient('mongo', 27017)
# Seleccionamos BD
db = client.movies
# Seleccionamos collection
pelis = db.pelis

# Inicialmente entramos en el formulario
def main_pymongo(request): return render(request, 'ejercicios/formulario.html')

# Procesamos la info del formulario
def consultas_pymongo(request):
	lista = []
	pelicula = request.POST.get('pelicula')
	anio = request.POST.get('anio')
	actor = request.POST.get('actor')

	er_pelicula = re.compile("^" + pelicula)
	er_anio = re.compile(anio)
	er_actor = re.compile("^" + actor)

	if pelicula != "" and anio != "" and actor != "":
		lista = pelis.find({
			'title': er_pelicula,
			'year': int(anio),
			'actors': er_actor
		})
	elif pelicula != "" and anio != "":
		lista = pelis.find({
			'title': er_pelicula,
			'year': int(anio)
		})
	elif pelicula != "" and actor != "":
		lista = pelis.find({
			'title': er_pelicula,
			'actors': er_actor
		})
	elif anio != "" and actor != "":
		lista = pelis.find({
			'year': int(anio),
			'actors': er_actor
		})
	elif pelicula != "":
		lista = pelis.find({
			'title': er_pelicula
		})
	elif anio != "":
		lista = pelis.find({
			'year': int(anio),
		})
	elif actor != "":
		lista = pelis.find({
			'actors': er_actor
		})

	context = {
		'lista': lista
	}

	return render(request, 'ejercicios/info_peliculas.html', context)

