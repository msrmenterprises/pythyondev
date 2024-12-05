# filename: check_weather_alternative.py
from pyowm import OWM

owm = OWM("YOUR_OWM_API_KEY")
mgr = owm.weather_manager()

observation = mgr.weather_at_place("Dallas,US")
w = observation.weather

weather = w.status
temperature = w.temperature('celsius')['temp']

print(f"The weather in Dallas, Texas is currently: {weather}")
print(f"The temperature is: {temperature}°C")