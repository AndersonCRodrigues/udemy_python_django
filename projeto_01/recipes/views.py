from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Anderson C Rodrigues'
    })


def contato(request):
    return HttpResponse('Contato')
