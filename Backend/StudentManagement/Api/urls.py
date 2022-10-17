from django.urls import path
from .views import student, home
urlpatterns = [

    path('student/login', student.login),
    path('student/signup', student.signup),
    path('', home)
]
