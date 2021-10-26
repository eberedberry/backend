from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default = 10)
    author = models.CharField(max_length= 300)
    body = models.TextField()
    date = models.DateTimeField()
    isbn = models.CharField(max_length=42, null = True, blank = True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    location = models.CharField(max_length=300)
    course =  models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name } from {self.location}"

    

