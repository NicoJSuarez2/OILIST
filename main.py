import requests
from tabpy.tabpy_tools.client import Client

def get_weather(city):
    api_key = "3c446fc59c3b7033549c816b13c2cd67"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"
    
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        return temperature, pressure, humidity, weather_description
    else:
        return None, None, None, "City Not Found"

# Registrar la función con TabPy
client = Client('http://localhost:9004/')
client.deploy('get_weather', get_weather, 'Returns weather data for a given city', override=True)

print("Function deployed successfully!")