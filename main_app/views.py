from django.shortcuts import render

from django.http import HttpResponse

class Plant:
    def __init__(self, name, description, age):
        self.name = name
        self.description = description
        self.age = age

plants = [
    Plant('Pothos', "The Pothos plant can be hung from a basket or potted normally, and can thrive in a wide variety of lighting. They are also known for their air-purification properties and can strip your home of toxins that are known to form in carpets and rugs.", 3),
    Plant('Fiddle Leaf Fig', "The fiddle leaf fig is great for apartments with high ceilings but minimal floor space. The plant is tall but not bushy, and boasts waxy, dark green leaves. It requires medium light, but only needs to be watered when the soil is dry to the touch.", 0),
    Plant('Cactus', "They're funky and non-fussy, and are probably the poster plants for non-garden environments. Cacti only require watering once a week while growing, but during cooler weather in the winter months, watering intervals may be longer. Place in a sunny area but keep out of direct sunlight, which can make the cactus look bleached or even orange.", 2)
    
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', { 'plants': plants })