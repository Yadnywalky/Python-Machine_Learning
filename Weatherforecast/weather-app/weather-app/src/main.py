import os
from dotenv import load_dotenv
from tkinter import Tk, Label, Entry, Button, messagebox, Canvas
from datetime import datetime
from services.weather_service import WeatherService
from utils.helpers import log_error
from PIL import Image, ImageTk
import threading

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("900x900")

        # Load and display background image
        self.bg_image = Image.open("F:/360_F_839844051_savJkwrT8vhPaMcAqu96fA80rn9yKnAr-transformed.jpeg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Bind the configure event to resize the background image
        self.root.bind("<Configure>", self.resize_bg)

        # Create a stylish label for entering the city name
        self.city_label = Label(root, text=" Enter City Name: ", bg="lightblue", font=("Helvetica", 16, ""), fg="white", relief="solid", bd=0)
        self.city_label.place(relx=0.5, rely=0.3, anchor="center")

        # Add shadow effect to the label
        self.shadow_label = Label(root, text=" Enter City Name: ", bg="lightblue", font=("Helvetica", 16, ""), fg="black", relief="solid", bd=1.5)
        self.shadow_label.place(relx=0.502, rely=0.302, anchor="center")

        # Create an entry widget for the city name with centered text
        self.city_entry = Entry(root, font=("Helvetica", 12), justify='center')
        self.city_entry.place(relx=0.5, rely=0.4, anchor="center")

        self.fetch_button = Button(root, text=" Fetch Weather ", command=self.start_fetch_weather, bg="lightblue", font=("Helvetica", 12))
        self.fetch_button.place(relx=0.5, rely=0.5, anchor="center")

        # Bind hover events to the fetch button
        self.fetch_button.bind("<Enter>", self.on_enter)
        self.fetch_button.bind("<Leave>", self.on_leave)

        # Create labels for displaying weather information
        self.temperature_label = Label(root, text="", bg="lightblue", font=("Helvetica", 12))
        self.temperature_label.place(relx=0.2, rely=0.6, anchor="center")

        self.wind_speed_label = Label(root, text="", bg="lightblue", font=("Helvetica", 12))
        self.wind_speed_label.place(relx=0.4, rely=0.6, anchor="center")

        self.humidity_label = Label(root, text="", bg="lightblue", font=("Helvetica", 12))
        self.humidity_label.place(relx=0.6, rely=0.6, anchor="center")

        self.description_label = Label(root, text="", bg="lightblue", font=("Helvetica", 12))
        self.description_label.place(relx=0.8, rely=0.6, anchor="center")

        self.datetime_label = Label(root, text="", bg="lightblue", font=("Helvetica", 12))
        self.datetime_label.place(relx=0.5, rely=0.7, anchor="center")

    def on_enter(self, event):
        self.fetch_button.config(bg="white")

    def on_leave(self, event):
        self.fetch_button.config(bg="lightblue")

    def resize_bg(self, event):
        new_width = event.width
        new_height = event.height
        self.bg_image_resized = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_photo_resized = ImageTk.PhotoImage(self.bg_image_resized)
        self.bg_label.config(image=self.bg_photo_resized)
        self.bg_label.image = self.bg_photo_resized

    def start_fetch_weather(self):
        threading.Thread(target=self.fetch_weather).start()

    def fetch_weather(self):
        city = self.city_entry.get()
        load_dotenv()
        api_key = os.getenv("WEATHER_API_KEY")

        if not api_key:
            messagebox.showerror("Error", "Please set the WEATHER_API_KEY environment variable.")
            return

        weather_service = WeatherService(api_key)
        try:
            weather_data = weather_service.fetch_weather(city)
            weather_info = weather_service.parse_weather(weather_data)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Update labels with weather information
            self.temperature_label.config(text=f"Temperature: {weather_info.temperature}°C")
            self.wind_speed_label.config(text=f"Wind Speed: {weather_info.wind_speed} m/s")
            self.humidity_label.config(text=f"Humidity: {weather_info.humidity}%")
            self.description_label.config(text=f"Description: {weather_info.description}")
            self.datetime_label.config(text=f"Date & Time: {current_time}")

        except Exception as e:
            log_error(str(e))
            messagebox.showerror("Error", "An error occurred while fetching the weather data.")

def main():
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()