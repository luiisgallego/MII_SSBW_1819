from django.shortcuts import render
from django.shortcuts import HttpResponse


def hola_mundo(request):
    salida = '''<html>Hola mundo</html>'''
    return HttpResponse(salida)


def ejercicio_1(request, usuario):
    salida = '''<html>Hola mundo %s</html>''' % (usuario)
    return HttpResponse(salida)