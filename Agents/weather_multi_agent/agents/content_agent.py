from pyexpat import model
from openai import api_key
from phi.agent import Agent
from phi.model.google import Gemini
from dotenv import load_dotenv
load_dotenv()

content_agent = Agent(
    name="Content Agent",
    role="Convert weather data into human-readable text",
    model = Gemini(model_name="gemini-1.5-flash",api_key=GOOGLE_API_KEY)
)

def generate_weather_summary(weather_data):
    if "error" in weather_data:
        return weather_data["error"]

    summary = (
        f"The current weather in {weather_data['city']} is "
        f"{weather_data['temperature']}°C with "
        f"{weather_data['condition']}. "
        f"The humidity level is around {weather_data['humidity']}%, "
        f"making the atmosphere comfortable."
    )

    return summary
