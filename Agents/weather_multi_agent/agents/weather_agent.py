from phi.agent import Agent
from utils.weather_api import get_weather
from content_agent import model

weather_agent = Agent(
    name="Weather Agent",
    role="Fetch real-time weather data using Weather API",
    model=model
   

def run_weather_agent(city):
    return get_weather(city)
