from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Todo
from .serializer import StudentSerializer, TodoSerializer

# Create your views here.

class StudentsViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

