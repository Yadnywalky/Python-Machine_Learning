import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.getenv("WEATHER_API_KEY")
    
    if not api_key:
        print("Error: Please set the WEATHER_API_KEY environment variable.")
        return

    print("Welcome to the Weather Application!")
    city = input("Enter the city name: ")
    
    from services.weather_service import WeatherService
    weather_service = WeatherService(api_key)
    
    try:
        weather_data = weather_service.fetch_weather(city)
        weather_info = weather_service.parse_weather(weather_data)
        
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_info.temperature}°C")
        print(f"Humidity: {weather_info.humidity}%")
        print(f"Description: {weather_info.description}")
    except Exception as e:
        from utils.helpers import log_error
        log_error(str(e))
        print("An error occurred while fetching the weather data.")

if __name__ == "__main__":
    main()