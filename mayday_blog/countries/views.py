from django.shortcuts import render
from django.http import HttpResponse


def index(requerst):
    return render(requerst, 'countries/index.html')
