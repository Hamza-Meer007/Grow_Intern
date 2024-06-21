from api import api_key  # for security purpose I do this
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
    else:
        print("City Not Found")


city = input("Enter city name: ")
get_weather(api_key, city)
