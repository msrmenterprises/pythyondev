# filename: get_weather_updated.py
import requests

# API key for OpenWeatherMap (you can obtain your own by signing up at https://home.openweathermap.org/users/sign_up)
api_key = "YOUR_API_KEY"

# City for which we want to get the weather
city = "Dallas"

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Making the request and getting the response
response = requests.get(url)
data = response.json()

# Checking if 'weather' key exists in the response
if 'weather' in data:
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    # Printing the weather information
    print(f"The weather in {city} is currently {weather_description}.")
    print(f"The temperature is {temperature} degrees Celsius and the humidity is {humidity}%.")
else:
    print("Weather information not available.")
