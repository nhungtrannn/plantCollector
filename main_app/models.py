from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

WATER = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Pot(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pots_detail', kwargs={'pk': self.id})

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    pots = models.ManyToManyField(Pot)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

    def watered_for_today(self):
        return self.watering_set.filter(date=date.today()).count() >= len(WATER)


class Watering(models.Model):
  date = models.DateField('watering date')
  water = models.CharField(
    max_length=1,
    choices=WATER,
    default=WATER[0][0]
  )

  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_water_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for plant_id: {self.plant_id} @{self.url}"