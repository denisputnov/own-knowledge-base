from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
	api_key = 'cd4894fa6fe57413646a3d6d029c3967'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()
	
	all_cities = list()

	for city in cities:
		res = requests.get(url.format(city)).json()
		city_info = {
			'city': city.name,
			'temp': res['main']['temp'],
			'icon': res['weather'][0]['icon']
		}

		all_cities.append(city_info)

	context = {'all_info': all_cities, 'form': form}

	return render(request, "weather/index.html", context)