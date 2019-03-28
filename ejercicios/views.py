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
	# HACERRRRRR!!!!
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
	titulos = re.findall(r'<title><\!\[CDATA\[(.+?)\]\]><\/title>', data)
	urlImagenes = re.findall(r'<enclosure url="(.+?)"', data)

	# for valor1, valor2 in zip(titulos, urlImagenes):
	# 	aux4.append({
	# 		'titulo:': valor1,
	# 		'imagen': valor2
	# 	})

	# for i in range(len(urlImagenes)):
	# 	aux4.append({
	# 		'titulo:': titulos[i],
	# 		'imagen': urlImagenes[i]
	# 	})

	aux2 = []
	for aux in titulos:
		aux2.append({'titulo': aux})
	
	aux3 = []
	for aux in urlImagenes:
		aux3.append({'titulo': aux})

	#####
	context = {
		'año': 2019,
		'lista': [
			{'nombre': 'pepe', 'numero': 2},
			{'nombre': 'miguel', 'numero': 3}
		],
		'titulos': titulos,
		'urlImagenes': aux3
	}

	return render(request, 'nombres.html', context)

############### TAREA 4 ################

client = MongoClient('mongo', 27017)
db = client.movies
pelis = db.pelis

def consultas_pymongo(request):
	lista = []
	lista = pelis.find(limit=10)
	print(pelis.count_documents({}))
	print(lista)
	context = {
		'lista': lista
	}
	# Hacer template !!!!!!
	return render(request, "salida.html", context)

	
