from django.shortcuts import render

def index(request):
    return JsonResponse({'name':'dimitri'})
# Create your views here.
