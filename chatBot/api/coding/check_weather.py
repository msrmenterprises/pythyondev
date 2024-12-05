# filename: check_weather.py
import requests

# Get the weather information from an API
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Dallas,US&appid=YOUR_API_KEY")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"The weather in Dallas, Texas is currently: {weather}")
    print(f"The temperature is: {temperature} Kelvin")
else:
    print("Could not retrieve weather information.")