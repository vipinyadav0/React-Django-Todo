from rest_framework import serializers
from .models import (Student, Family, Todo)

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    family = FamilySerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['name', 'address', 'school', 'family',]

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title","description","completed")
