
from django.http import JsonResponse, HttpResponse, HttpRequest
from types import SimpleNamespace
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

student = SimpleNamespace()


@api_view(["POST"])
def signup(req):

    print("####")
    print(req.data)
    return Response({"name": "Arque"})


student.signup = signup


@api_view(["POST"])
def login(req):

    print("####")
    print(req.data)
    return Response({"name": "Arque"})


student.login = login


@api_view(["GET", "POST"])
def home(req):
    return Response()
