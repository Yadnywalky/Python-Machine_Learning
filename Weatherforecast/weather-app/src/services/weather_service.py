class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, city):
        import requests
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error fetching weather data")

    def parse_weather(self, data):
        from src.models.weather_model import Weather
        weather = Weather()
        weather.temperature = data['main']['temp']
        weather.humidity = data['main']['humidity']
        weather.description = data['weather'][0]['description']
        return weather