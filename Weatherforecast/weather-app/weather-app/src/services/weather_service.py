import requests
from models.weather_model import Weather

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def parse_weather(self, data):
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        return Weather(temperature, wind_speed, humidity, description)