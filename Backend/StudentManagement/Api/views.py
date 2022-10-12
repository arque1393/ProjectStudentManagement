from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
def student():
    return JsonResponse(
        """
        {"Name": "Arque"}
        """
    )

def home(req):
    return HttpResponse("")