import requests
from datetime import datetime


def get_weather():
    now = datetime.now()
    date_time = now.strftime("%d %B %H:%M")
    response = requests.get("https://wttr.in/Minsk?format=%t")
    temperature = response.text
    print(f"The weather in minsk {date_time}:")
    print(temperature)


get_weather()
