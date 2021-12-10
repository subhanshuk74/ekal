from django.db import models
from django.urls import reverse

# Create your models here.
class student(models.Model,):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length = 100)
    Number=models.CharField(max_length = 10)

    def __str__(self):
        return self.Name