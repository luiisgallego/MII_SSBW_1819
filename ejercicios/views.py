from django.shortcuts import render
from django.shortcuts import HttpResponse

############### TAREA 1 ################

def hola_mundo(request):
    salida = '''<html>Hola mundo</html>'''
    return HttpResponse(salida)

def hola_mundo_nombre(request, usuario):
    salida = '''<html>Hola mundo %s</html>''' % (usuario)
    return HttpResponse(salida)

############### TAREA 2 ################

def ejercicio1(request):

    #salida = '''<html>Hola mundo ejercicio1</html>'''
    lista = ['hola', 'adios', 'yes']
    aux = 0

    for valor in lista:
        if len(valor) > 1:
            aux += 1
    
    return HttpResponse(aux)

############### TAREA 3 ################

def expresiones_regulares(request):

	context = {
		'año': 2019,
		'lista': [
			{'nombre': 'pepe', 'numero': 2},
			{'nombre': 'miguel', 'numero': 3}
		]
	}

	return render(request, 'nombres.html', context)