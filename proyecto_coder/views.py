from django.http import HttpResponse


def inicio(request):
    return HttpResponse('HOLA, estas en mi pagina web!')