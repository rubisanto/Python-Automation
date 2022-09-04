# API Key 7f590b390616cb236148b6d7a27fb2c2
# install pip install requests
import requests


API_KEY = "7f590b390616cb236148b6d7a27fb2c2"


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# choisir la ville
city = input("Enter the city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# send the request
response = requests.get(request_url)

# check the status code
if response.status_code == 200:
    data = response.json()
    # le temps général
    weather = data["weather"][0]["description"]
    # en calevin
    temperature1 = data["main"]["temp"]
    # en celsius arrondi à deux chiffres après la virgule
    temperature2 = round(temperature1 - 273.1, 2)
    print(f"weather: {weather}")
    print(f"temperature: {temperature2}")


else:
    print("Il y a eu une erreur")
