from tkinter import Tk, Label, StringVar, Button, Entry
from datetime import datetime
from services.weather_service import WeatherService

class WeatherApp:
    def __init__(self, master, api_key):
        self.master = master
        self.master.title("Weather Application")
        self.api_key = api_key
        
        self.city_var = StringVar()
        self.temperature_var = StringVar()
        self.wind_speed_var = StringVar()
        self.date_var = StringVar()
        self.time_var = StringVar()

        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text="Enter City:").pack()
        city_entry = Entry(self.master, textvariable=self.city_var)
        city_entry.pack()

        Button(self.master, text="Get Weather", command=self.get_weather).pack()

        Label(self.master, textvariable=self.temperature_var).pack()
        Label(self.master, textvariable=self.wind_speed_var).pack()
        Label(self.master, textvariable=self.date_var).pack()
        Label(self.master, textvariable=self.time_var).pack()

    def get_weather(self):
        city = self.city_var.get()
        weather_service = WeatherService(self.api_key)
        
        try:
            weather_data = weather_service.fetch_weather(city)
            weather_info = weather_service.parse_weather(weather_data)

            self.temperature_var.set(f"Temperature: {weather_info.temperature}°C")
            self.wind_speed_var.set(f"Wind Speed: {weather_info.wind_speed} m/s")
            self.date_var.set(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
            self.time_var.set(f"Time: {datetime.now().strftime('%H:%M:%S')}")
        except Exception as e:
            self.temperature_var.set("Error fetching weather data.")
            self.wind_speed_var.set("")
            self.date_var.set("")
            self.time_var.set("")

def run_app(api_key):
    root = Tk()
    app = WeatherApp(root, api_key)
    root.mainloop()