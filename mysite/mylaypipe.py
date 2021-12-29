from django.http import HttpResponse
from . import urls

def capitalize(request):
    return HttpResponse("capitalize")

def charcount(request):
    return HttpResponse("charcount")