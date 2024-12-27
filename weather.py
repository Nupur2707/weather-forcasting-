import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather details
def get_weather():
    city = city_entry.get().strip()  # Strip whitespace from input
    if not city:
        messagebox.showerror("Error", "City name cannot be empty!")
        return

    api_key = "9d671b2e8e47180078142418f13670e5"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        
        response = requests.get(base_url, params=params)
        data = response.json()

        # Handle API response
        if response.status_code == 200:
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            humidity = data['main']['humidity']
            result_label.config(
                text=f"City: {city.capitalize()}\nTemperature: {temp}°C\nWeather: {weather.capitalize()}\nHumidity: {humidity}%"
            )
        else:
            error_message = data.get("message", "Unknown error occurred")
            messagebox.showerror("Error", f"City '{city}' not found! ({error_message.capitalize()})")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error: {e}")
    except KeyError:
        messagebox.showerror("Error", "Unexpected response format from the API.")

# Setting up the GUI
app = tk.Tk()
app.title("Weather App")
app.geometry("300x300")
app.resizable(False, False)

# Input for city
city_label = tk.Label(app, text="Enter City:", font=("Arial", 12))
city_label.pack(pady=10)
city_entry = tk.Entry(app, font=("Arial", 12), width=20)
city_entry.pack(pady=5)

# Button to get weather
weather_button = tk.Button(app, text="Get Weather", font=("Arial", 12), command=get_weather)
weather_button.pack(pady=10)

# Label to display result
result_label = tk.Label(app, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)

app.mainloop()
