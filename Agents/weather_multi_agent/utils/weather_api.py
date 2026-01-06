import requests
import os
from dotenv import load_dotenv

from dotenv import load_dotenv
load_dotenv()

WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not WEATHER_API_KEY:
        return {"error": "API key not found. Please check .env file."}

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "City not found or API error"}

    data = response.json()

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"]
    }

    return weather_data
