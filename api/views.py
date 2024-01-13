from django.shortcuts import render

# Create your views here.
from .serializers import ProductSerializer, StudentSerializer
from .models import Product, Student
from rest_framework import viewsets

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer