from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return JsonResponse({'name':'dimitri'})

api_view('GET')
def first_api():
    query = Product.objects.all.orderby('?').first
    date={}
    if query:
        data = model_to_dict(query)
    return Response(data)
# Create your views here.
