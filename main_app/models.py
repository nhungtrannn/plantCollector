from django.db import models
from django.urls import reverse

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

def __str__(self):
        return self.name

def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})