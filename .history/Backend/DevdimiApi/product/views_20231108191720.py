from django.shortcuts import render
from django.http import JsonResponse


def index(request, *arg, **arg):
    return JsonResponse({'name':'dimitri'})
# Create your views here.
