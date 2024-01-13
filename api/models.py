from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField(default="Description", max_length=1000)
    image = models.ImageField(upload_to="Products", default="Products/products.png")
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "api"



class Student(models.Model):
    student_name = models.CharField(max_length=60)
    adm_no = models.CharField(max_length=10)
    books = models.TextField(default="List of books", max_length=1000)
    image = models.ImageField(upload_to="Students", default="Products/products.png")
    
    def __str__(self):
        return self.student_name


