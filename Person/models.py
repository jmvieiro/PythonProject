from datetime import date
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    date_created = models.DateField(auto_now_add=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return f'{self.name} {self.last_name}'